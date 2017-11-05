# -*- coding: utf-8 -*-
import json
import urllib2
import threading
import time
import datetime
import random
import os,sys
import cookielib
import urllib

CUR_PATH = os.path.abspath(sys.path[0])
host = '172.30.0.127'
port = '18001'


cookiejar = cookielib.CookieJar()
urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))     
def postJson(ipath,message={}):
    global cookiejar, urlOpener
    #print cookiejar 
    #print urlOpener
    requrl = 'http://' + host + ':' + port + ipath
    message_to_json = urllib.urlencode(message)
    header = {
        "Cache-Control": "no-cache",
        "cbxSource":"openplatform_cbx",
        "Pragma": "no-cache"}
    urlOpener.add_handler = [(k, v) for k, v in header.iteritems()]     
    try :    
        req = urllib2.Request(url=requrl, data=message_to_json, headers=header)
        print requrl
        print message_to_json
        res_data = urlOpener.open(req)
        res_data = res_data.read()
        #print res_data#.decode('utf-8')
        return res_data
    except Exception,e:
        print e
def postJsonAndImage(ipath,ddata):

    # import urllib2_file
    # import urllib2
    global cookiejar, urlOpener
    urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
    # header = {
    # "Content-type": "multipart/form-data; boundary",
    # "Cache-Control": "no-cache",
    # "cbxSource":"openplatform_cbx",
    # "Pragma": "no-cache"}
    # urlOpener.addheaders = [(k, v) for k, v in header.iteritems()] 

    boundary = '----------%s' % hex(int(time.time() * 1000))
    data = []
    data.append('--%s' % boundary)
    
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'des3msg')
    data.append(ddata["des3msg"])
    data.append('--%s' % boundary)
    
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'mac')
    data.append(ddata["mac"])
    data.append('--%s' % boundary)
    
    fr = open(CUR_PATH+'\sign.png','rb')
    data.append('Content-Disposition: form-data; name="%s"; filename="sign.png"' % 'signImg')
    data.append('Content-Type: %s\r\n' % 'image/png')
    data.append(fr.read())
    fr.close()    
    data.append('--%s' % boundary)
    
    http_body='\r\n'.join(data)
    header = {
    "Content-Type": "multipart/form-data; boundary=%s"%boundary,
    "Cache-Control": "no-cache",
    "cbxSource":"openplatform_cbx",
    "Pragma": "no-cache"}
    #print urlOpener.addheaders 
    urlOpener.addheaders = [(k, v) for k, v in header.iteritems()] 
    #print urlOpener.addheaders
    requrl = 'http://' + host + ':' + port + ipath
    print requrl
    try:
        request = urllib2.Request(url = requrl,headers=header,data =http_body)
        res_data = urlOpener.open(request).read()
        #print res_data#.decode('utf-8')
        return res_data   
    except Exception,e:
        print e
def log(line):
    log_handle.write(str(datetime.datetime.now()) + ' ' + line + '\n')    
    
class My_Thread(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)
    def run(self):
        # print '%s is running'%self.getName()
        begin = datetime.datetime.now()
        #rescode = pass

        end = datetime.datetime.now()
        thread_spend_time = (end - begin).total_seconds()
        st = str(thread_spend_time)
        if thread_spend_time>5:
            st = st+' '+'>5'
        else :
            st = st+' '+'<5'
        rlock.acquire()
        log('thread' +
            self.name +
            ' ' +
            'spendtime-->' +
            st
            )
        log(rescode)
        rlock.release()
if __name__ == '__main__':  
    randomNum = 'xxxxxxxx'
    orderNo = '99999999'
    des3msg = '{"settlementCycle":1,"paymentMethod":2,"randomNum":"%s","amount":5500,"longitude":113.93074927572707,"tradeType":1,"latitude":22.545664640286784,"clientType":"1","orderNo":"%s","goodsInfo":[{"isCustom":2,"price":5500}],"appCode":"1001050","trackBatchNo":"012345","pinBatchNo":"012345","deviceId":"00210101013600000329","cardNo":"439225******4935","clientVersion":"3.0.0","publicIndexNo":"01","track":"0922A6A95984BA3B8B6FA1D5578551C0F2F55F59CF1AEC26384F19AC50E88E99258F9B153B1D9722493BC1BACB37D2866CE99523C5BA8D79"}'%(randomNum,orderNo)
    #print des3msg
    mac = 'macmacmacmac'
    goodsOrderPaymentAndSignature_data = {
                                      "des3msg":des3msg,
                                      "mac":mac
                                        }
    goodsOrderPaymentAndSignature_path = '/cashbox/goodsOrderPaymentAndSignature.htm'
    
    postJsonAndImage(goodsOrderPaymentAndSignature_path,goodsOrderPaymentAndSignature_data)