import AES_hybrid
import time
import base64
with open("girl.jpg", "rb") as image_file:
    b1 = base64.b64encode(image_file.read())
b2 = 'ahdfsujeytsbsdfawskdfhsdgfereijd'
b3 = time.time()
b4 = AES_hybrid.encrypt(b2, b1)
b5 = time.time() - b3
print("Encryption time: {:.2f} seconds".format(b5))
with open("encry_test_Img.enc", "wb") as encrypted_file:
    encrypted_file.write(b4)
b6 = time.time()
b7 = AES_hybrid.decrypt(b2, b4)
b8 = time.time() - b6
print("Decryption time: {:.2f} seconds".format(b8))
with open("out_test_Img.jpeg", "wb") as decrypted_image_file:
    decrypted_image_file.write(base64.b64decode(b7))