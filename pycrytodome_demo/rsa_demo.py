#!/usr/bin/env python
# encoding:utf-8
from Crypto.PublicKey import RSA
code = 'nooneknows'
key = RSA.generate(2048)
encrypted_key = key.exportKey(passphrase=code, pkcs=8, 
        protection="scryptAndAES128-CBC")
with open('./path_to_private_key/my_private_rsa_key.bin', 'wb') as f:
    f.write(encrypted_key)

with open('./path_to_public_key/my_rsa_public.pem', 'wb') as f:
    f.write(key.publickey().exportKey())
	
'''
如果你希望使用 RSA 算法加密数据，那么你需要拥有访问 RAS 公钥和私钥的权限，否则你需要生成一组自己的密钥对。
在这个例子中，我们将生成自己的密钥对。创建 RSA 密钥非常容易，所以我们将在 Python 解释器中完成。
首先我们从 Crypto.PublicKey 包中导入 RSA，然后创建一个傻傻的密码。接着我们生成 2048 位的 RSA 密钥。现在我们到了关键的部分。
为了生成私钥，我们需要调用 RSA 密钥实例的 exportKey 方法，然后传入密码，使用的 PKCS 标准，以及加密方案这三个参数。之后，我们把私钥写入磁盘的文件中。

接下来，我们通过 RSA 密钥实例的 publickey 方法创建我们的公钥。我们使用方法链调用 publickey 和 exportKey 方法生成公钥，同样将它写入磁盘上的文件。
'''