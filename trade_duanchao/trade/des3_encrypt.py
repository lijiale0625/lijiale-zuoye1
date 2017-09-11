# -*- coding: utf-8 -*-
from pyDes import triple_des

def mac_padding(s):
    '''
    s       ：字符串
    
    补全方式：
    1、8的整数倍则补0x8000000000000000
    2、不是8的整数倍，则第一个字符补80,之后补00
    '''
    pad_len = 0
    total_len = 0
    i = 0
    length = len(s)
    #print length,'length'
    if (length %8):
        total_len = (length/8+1)*8
    else:
        total_len = length
    pad_len = total_len - length
    #print 'pad_len',pad_len
    if pad_len == 0 :
        pad_text = '8000000000000000'.decode('hex')
        return s+pad_text
    if pad_len == 1:
        pad_text = '80'.decode('hex')
    if pad_len>1 and pad_len<8:
        pad_text = '80'.decode('hex')+('00'.decode('hex'))*(pad_len-1)
    return s+pad_text
def padding(s):
    '''
    s：字符串
    补全方式：第一个字符补80,之后补00
    '''
    pad_len = 0
    total_len = 0
    i = 0
    length = len(s)
    #print length,'length'
    if (length %8):
        total_len = (length/8+1)*8
    else:
        total_len = length
    pad_len = total_len - length
    #print 'pad_len',pad_len
    if pad_len == 0 :
        return s
    if pad_len == 1:
        pad_text = '80'.decode('hex')
    if pad_len>1 and pad_len<8:
        pad_text = '80'.decode('hex')+'00'.decode('hex')*(pad_len-1)
    return s+pad_text  
def des3msg_encrypt(x,key):
    #print 'x->>>>>>>>>>>',x
    #print 'k->>>>>>>>>>>',key
    x = padding(x.encode('ascii'))
    #print 'x->>>>>>>>>>>',x
    key = triple_des(key)
    return key.encrypt(x).encode('hex').upper()
print des3msg_encrypt ('{"settlementCycle":1,"paymentMethod":2,"randomNum":"Efb9KzmYzH","amount":5500,"longitude":113.93074927572707,"tradeType":1,"latitude":22.545664640286784,"clientType":"1","orderNo":"968321342286815603","goodsInfo":[{"isCustom":2,"price":5500}],"appCode":"1001050","trackBatchNo":"012345","pinBatchNo":"012345","deviceId":"00210101013600000329","cardNo":"439225******4935","clientVersion":"3.0.0","publicIndexNo":"01","track":"0922A6A95984BA3B8B6FA1D5578551C0F2F55F59CF1AEC26384F19AC50E88E99258F9B153B1D9722493BC1BACB37D2866CE99523C5BA8D79"}'    ,'vwfrnvgNgezG27nY')
    
if __name__ == '__main__':  
    key1 = triple_des('H3GKE489AJEYwRt8')
    s = '{"settlementCycle":1,"paymentMethod":2,"randomNum":"qrK7vgfMQA","amount":5500,"longitude":113.93074927572707,"tradeType":1,"latitude":22.545664640286784,"clientType":"1","orderNo":"966550209779588017","goodsInfo":[{"isCustom":2,"price":5500}],"appCode":"1001050","trackBatchNo":"012345","pinBatchNo":"012345","deviceId":"00210101013200001094","cardNo":"439225******4935","clientVersion":"3.0.0","publicIndexNo":"01","track":"0922A6A95984BA3B8B6FA1D5578551C0F2F55F59CF1AEC26384F19AC50E88E99258F9B153B1D9722493BC1BACB37D2866CE99523C5BA8D79"}'
    s = padding(s)
    #print s
    cipher = key1.encrypt(s).encode('hex')
    #print cipher   
    s = '39DD691CF7EAE5EC0AE2483CF3F1C9B94257B42FE97B1EF34B98655835E2365AC2393789AC7B3BC9BC942DA4F3B4E4A7C33AE0E8EB3EAFBB5213C542AECE34373296466CC0200B074027C54F49DE6A68BE43E7F4EB5BC789181CCFEB74D4389132C692F8760071919FA9C1A24AC1A647225E2883C7853A3CAAC6567417DF63460218A2C59AAFC0DFEDCD419F61BB17133A446D67CA3E8FEE9AE2BDB4AA78620A978EAFB1A8C19BAC0B5F60AA5327E61D74C9E503ED46A13A6D6A14F4315BF6BF2DE379D11E91B3E9B298595063C23523605CF30C36090590F813E7136944A51B998271BC095F3D09E83D4ED06176B2F951E777325F5A05779B07D1A7E5B84800E1639426EB4E57833E1C3C8C51BA15699283BEFF7A523EE861597E193CD831A843414D8E6D28FD102CB948402059D5469B8F0A7C7E538E20F639032E035480AE2CFFADAE1A0B8E95D7D16982EB8412DBBDCB563D4196788DBC0ECBD8C9548C0AB477B9314F1F58820746E19131BB81EF217EA31E0DD033B400BE9FFF565A44E96BF8B9E39962DF32CC4BA1CC8B9943EF5C00C12A130C4AA63393BD488001D79EC314D2F0E6B8693E2EAAA42CFE8FD9AF68F64EAFA1CC1A4C1D6494DE28803F15E64220602B99E8FD17B1EBF1D804F6560A6CD1B76925080199DA23F00E1BAA0676B846022BA9C1D14ED2861FD56982C482267EA29C25B0B1A35FF8309833861914BDE4196FE4C466FDA3D208273EEB40BB824E0EE908B830EF5FD3E7F00F7083'
    #print key1.decrypt(s)
    
    

    
