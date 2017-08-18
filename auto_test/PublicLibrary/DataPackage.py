# coding=utf-8
from string import Template
from robot.api import logger

class data_package():
    # data_type 替换方式   data_body 数据体    parameter 参数
    def body_data_replace(self, data_body, parameter, data_type='1', call_back=0):
        '''body_data_replace 替换请求或响应
            | @{result} | body_data_replace | data_body | parameter | data_type |
        '''
        logger.info('data_body:%s \n parameter:%s \n data_type:%s \n call_back:%s' % (data_body, parameter, data_type ,str(call_back)))
        call_back += 1
        if len(parameter) !=0:
            data_body = str(data_body)
            if not isinstance(parameter, dict):
                parameter = eval(parameter)
            if data_type in ('1', 'local data', '2', 'database data'):       # 使用本地数据
                data_body = Template(data_body)
                data_body = data_body.safe_substitute(parameter).encode("utf-8")
                if int(data_body.count('$')) !=0 and call_back <=20:         # 控制回调次数
                    data_body = self.body_data_replace(data_body, parameter, data_type, call_back)
                return data_body
            elif data_type in ('0',  ''):
                return data_body
            else:
                return data_body
        else:
            return data_body

    def get_api_and_uri(self, host, uri):
        '''get_api_and_uri 分离请求地址中的主机地址和URI
            | @{result} | get_api_and_uri | host | uri |
        '''
        logger.info("host:%s  uri:%s" %(host, uri))
        uri_adder = uri.split('/')
        if uri_adder[0] in ('http:', 'https:'):
            host = uri_adder[0] + '//' + uri_adder[2]
            uri = ''
            for i in uri_adder[3:]:
                uri = uri + '/' + i
            logger.debug('host:%s  uri:%s' % (host, uri))
            return host, uri
        else:
            logger.debug('host:%s  uri:%s' % (host, uri))
            return host, uri

    # 处理SQL查询字段名
    def __query_filter(self, sql_content):
        result = []   # 保存处理后的字段名字
        if not isinstance(sql_content, str):
            sql_content = ' '.join(sql_content).split(',')
        for name in sql_content:
            if 'as' in name.lower().split():     # 有别名的数据
                start = name.lower().find('as')
                result.append(name[start + 2:].strip())
            elif '.' in name:                   # 处理带 *.
                start = name.find('.')
                result.append(name[start + 1:].strip())   # 处理普通
            else:
                result.append(name.strip())
        logger.debug('result:%s' % result)
        return result

    def basic_data_combination(self, table_lines_len, query_sql, *all_data):
        '''basic_data_combination 将查询结果保存为键值型式，以列名为key ,结果为值
            | @{result} | basic_data_combination | query_sql | table_lines_len | all_data |
        '''
        logger.debug('table_lines_len:%s' % table_lines_len)
        logger.debug('query_sql:%s' % query_sql)
        table_lines_len = int(table_lines_len)
        sql_content = query_sql.split(' ')
        for i in sql_content:
            if i.lower() == 'select':
                start_num = sql_content.index(i)
            if i.lower() == 'from':
                end = sql_content.index(i)
                break
        sql_content = self.__query_filter(sql_content[(start_num + 1): end])  # 获取到所有查询列名
        content = sql_content
        if '*' in sql_content:
            content = []
            for table_lines_info in all_data[table_lines_len:]:
                content.append((table_lines_info[0].lower()))
        logger.debug('current_content:%s' % content)
        table_all_lines_name_and_type = {}
        for lines_name in all_data[table_lines_len:]:    # 取表列名
            table_name = lines_name[0]
            table_name_type = lines_name[1]
            table_all_lines_name_and_type[table_name] = table_name_type
        print 'table_all_lines_name_and_type:',table_all_lines_name_and_type
        return_data = {}
        i=0
        for basic_data_one in all_data[0:1]:    # 只取一行的数据
            for basic_data in basic_data_one:
                logger.debug('basic_data:%s' % basic_data)
                return_data[content[i]] = basic_data
                i+=1
        return str(return_data)

    def get_sql_type(self, sql_statements):
        '''get_sql_type 分离请求地址中的主机地址和URI
            | @{result} | get_sql_type | ${sql_statements} |
        '''
        sql_statements = sql_statements.replace('\n','')
        sql_statements = sql_statements.replace('\r', '')
        sql_content = sql_statements.split(' ')
        logger.debug('sql_content[0]:%s' % sql_content[0])
        if sql_content[0].lower() in ('select'):
            return 'query_type'
        if sql_content[0].lower() in ('delete','insert','update'):
            return 'modify_type'

				
    def check_the_type(self, user, **data):
        '''check_the_type 获取数据库用户类型
            | ${result} | check_the_type | ${user} | &{data} |
        '''        
        if not isinstance(data, dict):
            data = eval(str(data))
        if user in data:
            return data[user]
        
        
if __name__ == '__main__':
    host = 'http://0.0.0.0:000'
    uri = 'https://172.16.0.216:8080/cashbox-sales-slip/payee/salesSlip/v1.json'
    data_body = '{"mobile":"${phone}", "cardId":"${id}"}'
    parameter = {"phone":"15919792521","id":"441827199203247211"}
    delete_query_sql = "delete tbl_sys_config t set t.sys_value='' where t.sys_key='new_product_send_slips_config_json'"
    select_query_sql = "select id, t.s, count(id),* from tbl_sys_config t  where t.sys_key='new_product_send_slips_config_json'"
    table_lines_len = '1'
    all_table = [(727, '013610399991', '05'),('ID', "<type 'cx_Oracle.NUMBER'>", 33, 22, 32, 0, 0), ('DEVICE_ID', "<type 'cx_Oracle.STRING'>", 25, 25, 0, 0, 0), ('DEVICE_OLD_VERSION', "<type 'cx_Oracle.STRING'>", 20, 20, 0, 0, 1)]
    all_table_2 = [('727'),('ID', "<type 'cx_Oracle.NUMBER'>", 33, 22, 32, 0, 0), ('DEVICE_ID', "<type 'cx_Oracle.STRING'>", 25, 25, 0, 0, 0), ('DEVICE_OLD_VERSION', "<type 'cx_Oracle.STRING'>", 20, 20, 0, 0, 1)]
    test = data_package()
    mode = 'time;from hashlib import md5;import os'
    test.quote_mode(mode)
    print test.check_the_type('id1', **parameter)
    #print test.basic_data_combination(table_lines_len, select_query_sql, *all_table)


