import AES_hybrid
import time
import base64
with open("girl.jpg", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())
start_time = time.time()
encrypted_data = AES_hybrid.encrypt('ahdfsujeytsbsdfawskdfhsdgfereijd', my_string)
print("Time for encryption: {} seconds".format(time.time() - start_time))
with open("encry_test_Img.enc", "wb") as enc_file:
    enc_file.write(encrypted_data)
start_time2 = time.time()
decrypted_data = AES_hybrid.decrypt('ahdfsujeytsbsdfawskdfhsdgfereijd', encrypted_data)
print("Time for decryption: {} seconds".format(time.time() - start_time2))
with open("out_test_Img.jpeg", "wb") as img_file:
    img_file.write(base64.b64decode(decrypted_data))