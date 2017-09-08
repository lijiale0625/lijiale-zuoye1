#!/usr/bin/env python
# encoding:utf-8

from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

with open('./path/to/encrypted_data.bin', 'wb') as out_file:
    recipient_key = RSA.import_key(
        open('./path_to_public_key/my_rsa_public.pem').read())
    session_key = get_random_bytes(16)

    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    out_file.write(cipher_rsa.encrypt(session_key))

    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    data = b'blah blah blah Python blah blah'
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)

    out_file.write(cipher_aes.nonce)
    out_file.write(tag)
    out_file.write(ciphertext)
	
'''
代码的前三行导入 PyCryptodome 包。然后我们打开一个文件用于写入数据。接着我们导入公钥赋给一个变量，创建一个 16 字节的会话密钥。在这个例子中，我们将使用混合加密方法，即 PKCS#1 OAEP ，也就是最优非对称加密填充。这允许我们向文件中写入任意长度的数据。接着我们创建 AES 加密，要加密的数据，然后加密数据。我们将得到加密的文本和消息认证码。最后，我们将随机数，消息认证码和加密的文本写入文件。

顺便提一下，随机数通常是真随机或伪随机数，只是用来进行密码通信的。对于 AES 加密，其密钥长度最少是 16 个字节。随意用一个你喜欢的编辑器试着打开这个被加密的文件，你应该只能看到乱码。
'''