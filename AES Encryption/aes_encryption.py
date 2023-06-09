from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# simple_key = get_random_bytes(32)
# print(simple_key)

x = b'\xc4\xc6\xc7\xfa\xa9\x98\xda\xf4\xab\xf1\xddi\x00\xc86j\xfe?\xac*\xbb:\xe4\x0e&J\x97C!~\xc2g'
password = "YashB63"

key = PBKDF2(password, x, dkLen=32)
#print(key)

message = "Hi Guys! Welcome to my Stream."

cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(message, AES.block_size))
#print(ciphered_data)

with open('encrypted.bin', 'wb') as f:
    f.write(cipher.iv)
    f.write(ciphered_data)
    
with open('encrypted.bin', 'rb') as f:
    iv = f.read(16)
    decrypt_data = f.read()
    
cipher = AES.new(key,  AES.MODE_CBC, iv=iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
print(original)

with open('key.bin', 'wb') as f:
    f.write(key)