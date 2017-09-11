#!/usr/bin/env python
# encoding:utf-8
from Crypto.Cipher import DES
key = 'abcdefgh'
def pad(text):
        while len(text) % 8 != 0:
            text += ' '
        return text
		
des = DES.new(key, DES.MODE_ECB)
text = 'Python rocks!'
encrypted_text = des.encrypt(padded_text)
print encrypted_text
encrypted_text = des.encrypt(padded_text.encode('utf-8'))
decrypted_text =des.decrypt(encrypted_text)
