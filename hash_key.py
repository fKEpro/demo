
# hashing


import hashlib
import binascii

plaintext = 'hello world from python'

# md5
md5 = hashlib.md5()
md5.update(plaintext.encode())
hash_md5 = md5.digest()
hex_hash_md5 = md5.hexdigest()
print('hash md5:', hash_md5)
print('hex hash md5:', hex_hash_md5)

# sha1
sha1 = hashlib.sha1()
sha1.update(plaintext.encode())
hash_sha1 = sha1.digest()
hex_hash_sha1 = sha1.hexdigest()
print('hash sha1:', hash_sha1)
print('hex hash sha1:', hex_hash_sha1)

# sha256
sha256 = hashlib.sha256()
sha256.update(plaintext.encode())
hash_sha256 = sha256.digest()
hex_hash_sha256 = sha256.hexdigest()
print('hash sha256:', hash_sha256)
print('hex hash sha256:', hex_hash_sha256)

# hash with key
# hmac
key = 'p4ssw0rd'
hmac = hashlib.pbkdf2_hmac('sha256', key.encode(), plaintext.encode(), 100000)
hex_hash_hmac = binascii.hexlify(hmac)
print('hex hash hmac:', hex_hash_hmac)

