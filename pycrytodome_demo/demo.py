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
padded_text = pad(text)
encrypted_text = des.encrypt(padded_text)
print encrypted_text
encrypted_text = des.encrypt(padded_text.encode('utf-8'))
print encrypted_text
decrypted_text =des.decrypt(encrypted_text)
print decrypted_text

'''
这段代码稍有些复杂，让我们一点点来看。首先需要注意的是，
DES 加密使用的密钥长度为 8 个字节，这也是我们将密钥变量设置为 8 个字符的原因。
而我们需要加密的字符串的长度必须是 8 的倍数，所以我们创建了一个名为 pad 的函数，
来给一个字符串末尾填充空格，直到它的长度是 8 的倍数。然后，我们创建了一个 DES 的实例，
以及我们需要加密的文本。我们还创建了一个经过填充处理的文本。我们尝试着对未经填充处理的文本进行加密，
啊欧，报了一个 ValueError 错误！我们需要对经过填充处理的文本进行加密，然后得到加密的字符串。
'''