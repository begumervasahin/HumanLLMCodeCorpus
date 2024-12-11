import AES_hybrid
import time
import base64
with open("girl.jpg", "rb") as img_file:
    b1 = base64.b64encode(img_file.read())
b2 = time.time()
b3 = AES_hybrid.encrypt('ahdfsujeytsbsdfawskdfhsdgfereijd', b1)
print("Time for encryption: {} seconds".format(time.time() - b2))
with open("encry_test_Img.enc", "wb") as enc_file:
    enc_file.write(b3)
b4 = time.time()
b5 = AES_hybrid.decrypt('ahdfsujeytsbsdfawskdfhsdgfereijd', b3)
print("Time for decryption: {} seconds".format(time.time() - b4))
with open("out_test_Img.jpeg", "wb") as img_file:
    img_file.write(base64.b64decode(b5))