from Crypto.Cipher import DES
from des3_encrypt import mac_padding
import binascii
import pyDes

    
    
def get_MAC(str,iv = b'\0\0\0\0\0\0\0\0'):
    k1 = pyDes.des('12345678')
    mac = list(iv)
    init = list(iv)
    str = mac_padding(str.encode('ascii'))#.encode('hex')
    bufLen = len(str)
    p = str
    #print p.encode('hex')
    while(bufLen>0):
        for i in range(8):
            #print p[i].encode('hex'),'----->',init[i].encode('hex')
            mac[i] = chr(ord(p[i])^ord(init[i]))
        #print mac    
        #print 'mac__>>encode',''.join(mac).encode('hex')
        mac = k1.encrypt(''.join(mac))  
        #print 'encrypt-->',mac
        mac = list(mac)
        init = mac
        p = p[8:]
        bufLen -= 8
    return ''.join(mac).encode('hex').upper()
print (get_MAC('{"settlementCycle":1,"paymentMethod":2,"randomNum":"Efb9KzmYzH","amount":5500,"longitude":113.93074927572707,"tradeType":1,"latitude":22.545664640286784,"clientType":"1","orderNo":"968321342286815603","goodsInfo":[{"isCustom":2,"price":5500}],"appCode":"1001050","trackBatchNo":"012345","pinBatchNo":"012345","deviceId":"00210101013600000329","cardNo":"439225******4935","clientVersion":"3.0.0","publicIndexNo":"01","track":"0922A6A95984BA3B8B6FA1D5578551C0F2F55F59CF1AEC26384F19AC50E88E99258F9B153B1D9722493BC1BACB37D2866CE99523C5BA8D79"}') )   
print (get_MAC(binascii.b2a_hex('579ED03C23FD74378839BA49D4A14F3F')))