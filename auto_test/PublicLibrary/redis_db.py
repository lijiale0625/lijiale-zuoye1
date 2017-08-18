# coding=utf-8
import redis
from robot.api import logger

class redis_db():
    # 保存连接对象
    def __int__(self):
        self.redis_db_connection = None

    # 连接数据库
    def connect_to_redis_db(self, connect_parameter):
        '''connect_to_redis_db 连接redis数据库
            | connect_to_redis_db | ${connect_parameter} |
        '''        
        if not isinstance(connect_parameter, dict):
            connect_parameter = eval(connect_parameter)
        for key, value in connect_parameter.items():
            if key == 'host':
                host = value
            elif key == 'port':
                port = value
        pool = redis.ConnectionPool(host = host, port = port)
        self.redis_db_connection = redis.Redis(connection_pool = pool)

    # 执行sql语法
    def execute_grammar(self, grammar, model):
        '''execute_grammar 执行redis的语句 model有二种：Don_it_need_to_return  need_to_return
            | @{result} | execute_grammar | ${grammar} | Don_it_need_to_return |
        '''          
        sql ='self.redis_db_connection.' + grammar
        logger.info('sql:%s' %sql)
        if model == 'Don_it_need_to_return':
            eval(sql)
            return {}
        elif model == 'need_to_return':
            results = {}
            key = self.get_key_name(grammar)
            str_key =str(key).replace('.', '_')
            results[str_key] = eval(sql)
            return results
        else:
            return {}

    # 获取查询的Key名称
    def get_key_name(self, grammar):
        '''get_key_name 获取查询的Key名称
            | @{result} | get_key_name | ${grammar} |
        '''        
        start_bit = grammar.find("(")
        end_bit = grammar.find(")")
        if grammar[start_bit:end_bit].find("'") !=-1:
            return grammar[start_bit +2:end_bit-1]
        else:
            return int(grammar[start_bit+1 :end_bit])

    # 分析语句的类型
    def analyze_redis_sql(self, grammar):
        '''analyze_redis_sql 分析语句的类型，判断是否需要保存结果
            | ${result} | analyze_redis_sql | ${grammar} |
        '''        
        end_bit = grammar.find('(')
        operation_way = grammar[0:end_bit]
        logger.debug('operation_way:%s' %operation_way)
        if operation_way in ('set', 'psetex', 'mset', 'hmset', 'setrange', 'setbit', 'bitop', 'incr' ,'incrbyfloat', 'decr',
                             'append', 'hset', 'hdel', 'hincrby', 'hincrbyfloat', 'lpush', 'rpush', 'lpushx','linsert',
                             'lset', 'lrem', 'ltrim', 'rpoplpush', 'brpoplpush', 'blpop', 'sadd', 'smove', 'spop', 'zadd',
                             'delete', 'expire'):
            return 'Don_it_need_to_return'
        elif operation_way in ('get', 'mget', 'getset', ' getrange', 'getbit', 'bitcount', 'strlen',  'hgetall',
                               'hlen', 'hkeys', 'hvals', 'hexists' ,'hscan', 'hscan_iter', 'lpop', 'lindex', 'scard',
                               'smembers', 'sscan', 'zcard', 'zrange', 'exists', 'keys', 'type', 'scan', 'hget'):
            return 'need_to_return'
        else:
            return 'not_find_type'

if __name__ == '__main__':
    #hostname = 'localhost'
    #service_port = 6379
    #hostname = '172.30.0.183'   #测试环境  172.30.0.179  172.30.0.181  172.30.0.183
    #service_port = 19000         #测试环境  6381  6380
    connet={"host":"localhost","port":"6379"}  # hmset('test',{'a':1,'b':2})
    #connet={"host":"172.30.0.183","port":"6380"}
    test_sql = "set('cashbox.sms.login.13444444457','test',ex=1)"
    test_sq2 = "get('cashbox.sms.login.13444444457')"

    test_sql3= "hmset('cashbox.sms.login.13444444458',{'aa':'11','b':'22'})"
    test_sql4= "hgetall('cashbox.sms.login.13444444457')"

    test_sql5 ="hset('foo_hash1','verifyCode','555555')"
    test_sql6 ="hgetall('foo_hash1')"

    test = redis_db()
    test.connect_to_redis_db(connet)
    # model=test.analyze_redis_sql(test_sql)
    # print 'model:',model
    # print test.execute_grammar(test_sql, model)
    # print '__________'

    model=test.analyze_redis_sql(test_sq2)
    print 'mode2:',model
    print test.execute_grammar(test_sq2, model)
    print '__________'

    # #
    # # model=test.analyze_redis_sql(test_sql5)
    # # print 'mode5:',model
    # # print test.execute_grammar(test_sql5, model)
    # # print '__________'
    # #
    # # model=test.analyze_redis_sql(test_sql6)
    # # print 'mode6:',model
    # # print test.execute_grammar(test_sql6, model)
    # # print '__________'
    # #
    # # model=test.analyze_redis_sql(test_sql3)
    # # print 'mode3:',model
    # # print test.execute_grammar(test_sql3, model)
    # # print '__________'
    #
    # model2=test.analyze_redis_sql(test_sql4)
    # print 'model4:',model2
    # print test.execute_grammar(test_sql4, model2)
