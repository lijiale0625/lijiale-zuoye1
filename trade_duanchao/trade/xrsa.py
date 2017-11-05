# -*- coding: utf-8 -*-
__author__ = 'luchanghong'
import rsa

# ������һ����Կ��Ȼ�󱣴�.pem��ʽ�ļ�����ȻҲ����ֱ��ʹ��
(pubkey, privkey) = rsa.newkeys(1024)

pub = pubkey.save_pkcs1()
pubfile = open('public.pem','w+')
pubfile.write(pub)
pubfile.close()

pri = privkey.save_pkcs1()
prifile = open('private.pem','w+')
prifile.write(pri)
prifile.close()

# load��Կ����Կ
message = 'hello'
with open('public.pem') as publickfile:
    p = publickfile.read()
    pubkey = rsa.PublicKey.load_pkcs1(p)

with open('private.pem') as privatefile:
    p = privatefile.read()
    privkey = rsa.PrivateKey.load_pkcs1(p)

# �ù�Կ���ܡ�����˽Կ����
crypto = rsa.encrypt(message, pubkey)

print type(crypto),crypto
message = rsa.decrypt(crypto, privkey)
print message

# sign ��˽Կǩ�����桢���ù�Կ��֤ǩ��
signature = rsa.sign(message, privkey, 'SHA-1')
rsa.verify('hello', signature, pubkey)