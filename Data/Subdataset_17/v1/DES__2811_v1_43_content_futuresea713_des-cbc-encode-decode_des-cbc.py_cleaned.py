import pyDes
import base64
data = "abc123"
key = 'g9G16nTs'
iv = 'g9G16nTs'
cipher = pyDes.des(key, pyDes.CBC, iv, pad=None, padmode=pyDes.PAD_PKCS5)
encrypted_data = cipher.encrypt(data)
encoded_encrypted_data = base64.b64encode(encrypted_data)
decoded_encrypted_data = base64.b64decode(encoded_encrypted_data)
decrypted_data = cipher.decrypt(decoded_encrypted_data)
print("Original Data:", data)
print("Encrypted (base64 encoded):", encoded_encrypted_data.decode())
print("Decrypted Data:", decrypted_data.decode())