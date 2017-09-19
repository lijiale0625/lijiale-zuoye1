#!/usr/bin/env python
# encoding:utf-8
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

code = 'nooneknows'

with open('./path/to/encrypted_data.bin', 'rb') as fobj:
    private_key = RSA.import_key(
        open('./path_to_private_key/my_private_rsa_key.bin').read(),
        passphrase=code)

    enc_session_key, nonce, tag, ciphertext = [ fobj.read(x) 
                                                for x in (private_key.size_in_bytes(), 
                                                16, 16, -1) ]

    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)

    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)

print(data)
'''
如果你认真看了上一个例子，这段代码应该很容易解析。
在这里，我们先以二进制模式读取我们的加密文件，然后导入私钥。
注意，当你导入私钥时，需要提供一个密码，否则会出现错误。
然后，我们文件中读取数据，首先是加密的会话密钥，然后是 16 字节的随机数和 16 字节的消息认证码，最后是剩下的加密的数据。

接下来我们需要解密出会话密钥，重新创建 AES 密钥，然后解密出数据。
'''