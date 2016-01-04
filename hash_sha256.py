
# crypto - hash


from Crypto.Hash import SHA256

plaintext = 'hello world from python'

sha256 = SHA256.new()
sha256.update(plaintext.encode())
hash_sha256 = sha256.digest()
hex_hash_sha256 = sha256.hexdigest()
print('hash sha256:', hash_sha256)
print('hex hash sha256:', hex_hash_sha256)

