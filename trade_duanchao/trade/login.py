# -*- coding: utf-8 -*-
import hashlib
import os
import json
import sys
import threading
import datetime
import time

import postMessage
from rsa_decrypt import decrytpWk
from des3_encrypt import des3msg_encrypt
from ebc import get_MAC
CUR_PATH = os.path.abspath(sys.path[0])

account =       '13928460255'
password =      hashlib.md5('111111').hexdigest().upper()
clientType =    'android'
clientVersion = '3.0.0'

login_path = '/fspf-cashbox/login.htm'
preTradeCondition_path = '/fspf-cashbox/v2/preTradeCondition.htm'
deviceAuth_path = '/fspf-cashbox/v3/deviceAuth.htm'
goodsOrderPaymentAndSignature_path = '/fspf-cashbox/goodsOrderPaymentAndSignature.htm'
login_data = {'account':account,
                  'password':password,
                  'clientType':clientType,
                  'clientVersion':clientVersion
                  #'name':name,
                  #'verifyCode':verifyCode,
                  #'mobile':mobile,
                  #'token':token,
                  #'isIwf':isIwf,
                  #'memberId':memberId
                  }
preTradeCondition_data = {
                    "type": "4",
                    "des3Key": "",
                    "mac": ""
                    }  
#0303001be1040000168bf986644a4840d48e62110da14e09be01360000032975d240  
#                  04bc8d694d54e37a4d3ab7b8c7355f76                  
deviceAuth_data = {
                    "deviceId":"00210101013600000329",
                    "randomNum":"dmFEm3eA",
                    "authFlag":"Auto",
                    "desMessage":"8bf986644a4840d48e62110da14e09be"
                    }    
#rsa解密密钥                    
rsa_public_key = '0084B13C5AF4370ECAAB4919EE840C9552534E28BE50B712CCF33EBCE25632A26E46B9EB5E13A2B6A0F5BF0162AFD835535DE3A826E387ADD482F1C715AC313CE4CE4CC8646669D06A65AF4C69BDA0BE3045CF77A54C4CB5869BE8F98461DD4428C9D34991E4FD8A9B9FDCEEF1B901F9272A94EB8547E28AA4212D13CB05B135C9'                    
#'463CF2E7F0802F75DD4A015CDAD680BEF81E2D59FF451A5FB94B8EE96A72D73A582D355FF832BDBEEF4D924C546C09E94C18113956336C8EE525849B60477E292F269295E3A0163721940AE2413D4507EA3790A47331FE053F29DAC6247F187EFDAC212C77DEBE7E4D142B4B468345BF8AC3378804474B5B050F18AF8A7C81E2'
#解密后为nALbT4r5BhL4RKQB
#[deviceId=00210101013200001093, randomNum=dmFEm3eA, authFlag=Auto, desMessage=04bc8d694d54e37a4d3ab7b8c7355f76]       

# goodsOrderPaymentAndSignature_data = {
                                      # 'des3msg':'%s'%cipher,
                                      # 'mac':''
                                        # }

def log(line):
    if line !=None:
        log_handle.write(str(datetime.datetime.now()) + ' ' + str(line) + '\n')
    else:    
        log_handle.write(str(datetime.datetime.now()) + ' ' + 'None' + '\n')
class MyThread(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)           
    def run(self):
        rlock = threading.RLock()
        begin = datetime.datetime.now()
        preTradeConditon_ret = json.loads(postMessage.postJson(preTradeCondition_path,preTradeCondition_data))
        print (preTradeConditon_ret)
        ret_status = preTradeConditon_ret["status"]
        if ret_status == "1":
            orderNo = preTradeConditon_ret["orderNo"]
            randomNum = preTradeConditon_ret["randomNum"]
        print (orderNo)
        print (randomNum)
        track = '3F24C19D4113E6FF900607AD908A75DE424A2C513E5BF04270652A379297E0A7BDD0E9F6316F0CB167ED066E0DB69CE5D25777AA50FBB83B33078F05EFAD35A4DB979D403DE9FB52B280236D0A098FE136F20CBEE4272E6AA566ECF800C9E960DE5F383CA3C6F04662E38C9671BB4DBC'
        des3msg = '{"settlementCycle":1,"paymentMethod":2,"randomNum":"%s","amount":5500,"longitude":113.93074927572707,"tradeType":1,"latitude":22.545664640286784,"clientType":"1","orderNo":"%s","goodsInfo":[{"isCustom":2,"price":5500}],"appCode":"1001050","trackBatchNo":"012345","pinBatchNo":"012345","deviceId":"00210101013600000329","cardNo":"6225******1128","clientVersion":"3.0.0","publicIndexNo":"01","track":"%s"}'%(randomNum,orderNo,track)    
        mac = get_MAC(des3msg)
        des3msg = des3msg_encrypt(des3msg,wk_decrypt)    
        goodsOrderPaymentAndSignature_data = {
                                          "des3msg":des3msg,
                                          "mac":mac
                                            } 
        goodsOrderPaymentAndSignature_ret = json.loads(postMessage.postJsonAndImage(goodsOrderPaymentAndSignature_path,goodsOrderPaymentAndSignature_data))
        print ('goodsOrderPaymentAndSignature_ret--------->',goodsOrderPaymentAndSignature_ret)
        ret_status = goodsOrderPaymentAndSignature_ret["responseCode"]
        errorMsg = goodsOrderPaymentAndSignature_ret["errorMsg"]
        cupCode = goodsOrderPaymentAndSignature_ret["cupCode"]
        if ret_status == '1' and cupCode == '00':
            print (u'交易成功')
        else:
            print (u'交易失败:',errorMsg)
        end = datetime.datetime.now()
        thread_spend_time = (end - begin).total_seconds()
        st = str(thread_spend_time)
        rlock.acquire()
        log('thread' +
            self.name +
            ' ' +
            'spendtime-->' +
            st
            )
        log(goodsOrderPaymentAndSignature_ret)
        rlock.release()                                        
def main():
    print ('step 1 begin','-'*40)        
    login_ret = json.loads(postMessage.postJson(login_path,login_data) )
    print (login_ret)
    ret_status = login_ret["status"]
    #print login_ret["name"]
    if ret_status == "1":
        print (u'登录成功,商户名称:',login_ret["name"])
        print (u'         手机号  :',login_ret["mobile"])
        print (u'         盒子列表:',login_ret["boxList"])
    else:
        print (u'登录失败')
        #sys.exit(1)
    print  ('step 1 end','-'*40,u'登录结束') 
    print
    print
    
    print ('step 2 begin','-'*40,u'设备认证' )
    deviceAuth_ret = json.loads(postMessage.postJson(deviceAuth_path,deviceAuth_data))
    print (deviceAuth_ret)
    ret_status = deviceAuth_ret["status"]
    if ret_status == "1":
        wk = deviceAuth_ret["wk"]
        print (u'获取workkey成功:',wk)
        wk_decrypt = decrytpWk(wk)
        print (u'workkey明文:',wk_decrypt)
    else:
        print (u'认证失败,workkey获取失败')
        sys.exit(1)
    print  ('step 2 end','-'*40,u'设备认证结束'   )     
    print
    print
    
    print ('step 3 begin','-'*40,u'获取订单号、随机数'   )  
    preTradeConditon_ret = json.loads(postMessage.postJson(preTradeCondition_path,preTradeCondition_data) )
    print (preTradeConditon_ret)
    ret_status = preTradeConditon_ret["status"]
    if ret_status == "1":
        orderNo = preTradeConditon_ret["orderNo"]
        randomNum = preTradeConditon_ret["randomNum"]
        print (u'获取成功,订单号:',orderNo)
        print (u'         随机数:',randomNum)
    print  ('step 3 end','-'*40,u'获取订单号、随机数结束' )
    print
    print
    
    # randomNum = 'xxxx'
    # orderNo = '99999'
    # wk_decrypt = 'xxxxxxxxxxxxxxxx'
    print ('step 4 begin','-'*40 )
    track = '3F24C19D4113E6FF900607AD908A75DE424A2C513E5BF04270652A379297E0A7BDD0E9F6316F0CB167ED066E0DB69CE5D25777AA50FBB83B33078F05EFAD35A4DB979D403DE9FB52B280236D0A098FE136F20CBEE4272E6AA566ECF800C9E960DE5F383CA3C6F04662E38C9671BB4DBC'
    #由于 track是根据wklmk解密的,密钥与生产一致,不可拿到。track每24小时更新一次,24小时后必须手动抓取更新
    des3msg = '{"settlementCycle":1,"paymentMethod":2,"randomNum":"%s","amount":5500,"longitude":113.93074927572707,"tradeType":1,"latitude":22.545664640286784,"clientType":"1","orderNo":"%s","goodsInfo":[{"isCustom":2,"price":5500}],"appCode":"1001050","trackBatchNo":"012345","pinBatchNo":"012345","deviceId":"00210101013600000329","cardNo":"6225******1128","clientVersion":"3.0.0","publicIndexNo":"01","track":"%s"}'%(randomNum,orderNo,track)
    #print des3msg
    mac = get_MAC(des3msg)
    des3msg = des3msg_encrypt(des3msg,wk_decrypt)    
    goodsOrderPaymentAndSignature_data = {
                                      "des3msg":des3msg,
                                      "mac":mac
                                        }
    goodsOrderPaymentAndSignature_ret = json.loads(postMessage.postJsonAndImage(goodsOrderPaymentAndSignature_path,goodsOrderPaymentAndSignature_data))
    print (goodsOrderPaymentAndSignature_ret)
    ret_status = goodsOrderPaymentAndSignature_ret["responseCode"]
    errorMsg = goodsOrderPaymentAndSignature_ret["errorMsg"]
    cupCode = goodsOrderPaymentAndSignature_ret["cupCode"]
    if ret_status == '1' and cupCode == '00':
        print (u'交易成功')
    else :
        print (u'交易失败,responseCode:',ret_status)
        print (u'错误码cupCode:')
        print (u'失败描述:',errorMsg)
        
    print ('step 4 end','-'*40   )                                                                           
if __name__ == '__main__':  
    print ('step 1 begin','-'*40 )       
    login_ret = json.loads(postMessage.postJson(login_path,login_data) )
    print (login_ret)
    ret_status = login_ret["status"]
    #print login_ret["name"]
    if ret_status == "1":
        print (u'登录成功,商户名称:',login_ret["name"])
        print (u'         手机号  :',login_ret["mobile"])
        print (u'         盒子列表:',login_ret["boxList"])
    else:
        print (u'登录失败')
        #sys.exit(1)
    print  ('step 1 end','-'*40,u'登录结束' )
    print
    print
    
    print ('step 2 begin','-'*40,u'设备认证' )
    deviceAuth_ret = json.loads(postMessage.postJson(deviceAuth_path,deviceAuth_data))
    print (deviceAuth_ret)
    ret_status = deviceAuth_ret["status"]
    if ret_status == "1":
        wk = deviceAuth_ret["wk"]
        print (u'获取workkey成功:',wk)
        wk_decrypt = decrytpWk(wk)
        print (u'workkey明文:',wk_decrypt)
    else:
        print (u'认证失败,workkey获取失败')
        sys.exit(1)
    print  ('step 2 end','-'*40,u'设备认证结束'    )    
    print
    print
    global log_handle
    log_handle = open(CUR_PATH + '\log.log', 'a+')
    t1 = []
    transaction = 1 #总事务数
    for i in range(transaction):
        t = MyThread(str(i))
        t1.append(t)
    x = 0
    for i in range(len(t1)):
        while True:
            if len(threading.enumerate()) <30:#并发数
                t1[i].start()
                break
            else:
                continue            
        if (i + 1) % 1 == 0:
            time.sleep(.1) 
            print ('*' * 20)
    while(True):
        if len(threading.enumerate()) > 1:
            # print threading.enumerate()
            time.sleep(1)
        else:
            break
    print ('----------------end post')
    log_handle.close()    