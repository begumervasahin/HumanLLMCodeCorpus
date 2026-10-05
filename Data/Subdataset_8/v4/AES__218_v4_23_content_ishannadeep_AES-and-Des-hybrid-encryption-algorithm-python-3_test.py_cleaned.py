import AES_hybrid
import time
import base64
with open("girl.jpg", "rb") as image_file:
    image_data = base64.b64encode(image_file.read())
encryption_key = 'ahdfsujeytsbsdfawskdfhsdgfereijd'
start_encryption_time = time.time()
encrypted_data = AES_hybrid.encrypt(encryption_key, image_data)
encryption_time = time.time() - start_encryption_time
print("Encryption time: {:.2f} seconds".format(encryption_time))
with open("encry_test_Img.enc", "wb") as encrypted_file:
    encrypted_file.write(encrypted_data)
start_decryption_time = time.time()
decrypted_data = AES_hybrid.decrypt(encryption_key, encrypted_data)
decryption_time = time.time() - start_decryption_time
print("Decryption time: {:.2f} seconds".format(decryption_time))
with open("out_test_Img.jpeg", "wb") as decrypted_image_file:
    decrypted_image_file.write(base64.b64decode(decrypted_data))