import AES_hybrid
import time
import base64
def fonk1(file_path):
    with open(file_path, "rb") as image_file:
        return base64.b64encode(image_file.read())
def fonk2(b7, key):
    b1 = time.time()
    b2 = AES_hybrid.encrypt(key, b7)
    b3 = time.time() - b1
    print("Encryption completed in: {} seconds".format(b3))
    return b2
def fonk3(file_path, data):
    with open(file_path, "wb") as file:
        file.write(data)
def fonk4(b2, key):
    b1 = time.time()
    b4 = AES_hybrid.decrypt(key, b2)
    b5 = time.time() - b1
    print("Decryption completed in: {} seconds".format(b5))
    return b4
def fonk5(file_path, data):
    with open(file_path, "wb") as image_file:
        image_file.write(base64.b64decode(data))
if b6 = = "__main__":
    b7 = fonk1("girl.jpg")
    b8 = 'ahdfsujeytsbsdfawskdfhsdgfereijd'
    b2 = fonk2(b7, b8)
    fonk3("encry_test_Img.enc", b2)
    b4 = fonk4(b2, b8)
    fonk5("out_test_Img.jpeg", b4)