#!/usr/bin/env python
# encoding:utf-8
from cryptography.fernet import Fernet
cipher_key = Fernet.generate_key()
print cipher_key
cipher = Fernet(cipher_key)
text = b'My super secret message'
encrypted_text = cipher.encrypt(text)
print encrypted_text
decrypted_text = cipher.decrypt(encrypted_text)
print decrypted_text

'''
首先我们需要导入 Fernet，然后生成一个密钥。我们输出密钥看看它是什么样儿。如你所见，它是一个随机的字节串。如果你愿意的话，可以试着多运行 generate_key 方法几次，生成的密钥会是不同的。然后我们使用这个密钥生成 Fernet 密码实例。

现在我们有了用来加密和解密消息的密码。下一步是创建一个需要加密的消息，然后使用 encrypt 方法对它加密。我打印出加密的文本，然后你可以看到你再也读不懂它了。为了解密出我们的秘密消息，我们只需调用 decrypt 方法，并传入加密的文本作为参数。结果就是我们得到了消息字节串形式的纯文本。
'''