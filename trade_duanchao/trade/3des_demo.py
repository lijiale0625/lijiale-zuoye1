# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import os

# 在进行加密/解密前，只需使用 pad/unpad 进行填充/截断即可
BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)#匿名函数
unpad = lambda s : s[0:-ord(s[-1])]
 # 生成随机密码
key = os.urandom(16) # the length can be (16, 24, 32)
text = 'qingyejin'  #加密内容
 
cipher = AES.new(key)
print (pad(text))
encrypted = cipher.encrypt(pad(text)).encode('hex')
print (encrypted)  # will be something like 'f456a6b0e54e35f2711a9fa078a76d16'
decrypted = unpad(cipher.decrypt(encrypted.decode('hex')))
print ('decrypted::______>',decrypted)  # will be 'to be encrypted'
