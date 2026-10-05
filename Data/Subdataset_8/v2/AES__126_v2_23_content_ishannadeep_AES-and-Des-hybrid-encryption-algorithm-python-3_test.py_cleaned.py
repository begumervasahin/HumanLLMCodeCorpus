import AES_hybrid
import time
import base64
with open("girl.jpg", "rb") as image_file:
    image_data = base64.b64encode(image_file.read())
start_time = time.time()
encryption_key = 'ahdfsujeytsbsdfawskdfhsdgfereijd'
encrypted_data = AES_hybrid.encrypt(encryption_key, image_data)
encryption_time = time.time() - start_time
print("Encryption completed in: {} seconds".format(encryption_time))
with open("encry_test_Img.enc", "wb") as encrypted_file:
    encrypted_file.write(encrypted_data)
start_time2 = time.time()
decrypted_data = AES_hybrid.decrypt(encryption_key, encrypted_data)
decryption_time = time.time() - start_time2
print("Decryption completed in: {} seconds".format(decryption_time))
with open("out_test_Img.jpeg", "wb") as decrypted_image_file:
    decrypted_image_file.write(base64.b64decode(decrypted_data))