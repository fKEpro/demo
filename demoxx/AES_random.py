# crypto - Symmetric Cryptography

from Crypto import Random
from Crypto.Cipher import AES

message = 'hey,man'
# AES key must be either 16, 24, or 32 bytes long
key = 'p4ssw0rdp4ssw0rdp4ssw0rdp4ssw0rd'
print('message:', message)

# encrypt
iv_aes = Random.new().read(AES.block_size)
cipher_aes = AES.new(key.encode(), AES.MODE_CFB, iv_aes)
encrypted_aes = cipher_aes.encrypt(message.encode())
print('encrypted AES:', encrypted_aes)


# decrypted
dec_iv_aes = Random.new().read(AES.block_size)
dec_cipher_aes = AES.new(key.encode(), AES.MODE_CFB, iv_aes)
decrypted_aes = dec_cipher_aes.decrypt(encrypted_aes)
print('decrypted AES:', decrypted_aes)

