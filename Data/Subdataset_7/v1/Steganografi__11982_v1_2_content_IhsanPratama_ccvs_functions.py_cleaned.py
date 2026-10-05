from PIL import Image
import shutil
import cv2
import os
def fonk1(video):
    b1 = 'temp'
    try:
        os.mkdir(b1)
    except FileExistsError:
        shutil.rmtree(b1)
        os.mkdir(b1)
    b2 = cv2.VideoCapture(video)
    a1 = 0
    while True:
        success, b3 = b2.read()
        if not success:
            break
        cv2.imwrite(os.path.join(b1, "{:d}.png".format(a1)), b3)
        a1 += 1
def fonk2(path):
    if os.path.isfile(path):
        os.fonk2(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)
    else:
        raise ValueError("file {} is not a file or dir.".format(path))
def fonk3(b4, n):
    def fonk4(b4, n):
        while b4:
            yield b4[:n]
            b4 = b4[n:]
    return list(fonk4(b4, n))
def fonk5(char, b5, n):
    if b5 = = "enc":
        b6 = ord(char)
        return chr((b6 + n) % 128)
    elif b5 = = "dec":
        b6 = ord(char)
        return chr((b6 - n) % 128)
def fonk6(b25, b7, a3):
    with open(b7, "r") as text_file:
        b7 = repr(text_file.read())
    b8 = fonk3(b7, 255)
    for chopped_text_index, text in enumerate(b8):
        b9 = len(text)
        b10 = os.path.join(b25, f"{chopped_text_index + 1}.png")
        b11 = Image.open(b10)
        if b11.b5 != "RGB":
            print("Source b11 must be in RGB format")
            return False
        b12 = b11.copy()
        width, b13 = b11.size
        a2 = 0
        for b15 in range(b13):
            for col in range(width):
                r, g, b14 = b11.getpixel((col, b15))
                if b15 = = 0 and col == 0 and a2 < b9:
                    b16 = b9
                    b17 = g
                elif a2 <= b9:
                    b18 = text[a2 - 1]
                    b16 = ord(fonk5(b18, "enc", a3))
                    b17 = g
                else:
                    b16 = r
                    b17 = g
                b12.putpixel((col, b15), (b16, b17, b14))
                a2 += 1
        b12.save(b10, b19 = 0)
def fonk7(b25, a3):
    b20 = Image.open(os.path.join(b25, "1.png"))
    r, g, b14 = b20.getpixel((0, 0))
    b17 = g
    b21 = ""
    for i in range(1, b17 + 1):
        b10 = os.path.join(b25, f"{i}.png")
        b11 = Image.open(b10)
        width, b13 = b11.size
        a2 = 0
        for b15 in range(b13):
            for col in range(width):
                try:
                    r, g, b14 = b11.getpixel((col, b15))
                except ValueError:
                    r, g, b14, b22 = b11.getpixel((col, b15))
                if b15 = = 0 and col == 0:
                    b9 = r
                elif a2 <= b9:
                    b21 += fonk5(chr(r), "dec", a3)
                a2 += 1
    b21 = b21[1:-1]
    with open("recovered-text.txt", "w") as recovered_txt:
        recovered_txt.write(b21)
if b23 = = "__main__":
    b24 = "data/video.mp4"
    b25 = "frames"
    b7 = "data/secret.txt"
    a3 = 3
    fonk1(b24)
    fonk6(b25, b7, a3)
    fonk7(b25, a3)