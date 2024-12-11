from PIL import Image
import shutil
import cv2
import os
def fonk1(video_path):
    b1 = 'temp'
    try:
        os.mkdir(b1)
    except FileExistsError:
        shutil.rmtree(b1)
        os.mkdir(b1)
    b2 = cv2.VideoCapture(video_path)
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
        raise ValueError("The path {} does not point to a file or directory.".format(path))
def fonk3(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]
def fonk4(char, b4, shift):
    if b4 = = "enc":
        b5 = ord(char)
        return chr((b5 + shift) % 128)
    elif b4 = = "dec":
        b5 = ord(char)
        return chr((b5 - shift) % 128)
def fonk5(b24, text_path, shift):
    with open(text_path, "r") as text_file:
        b6 = repr(text_file.read())
    b7 = fonk3(b6, 255)
    for index, chunk in enumerate(b7):
        b8 = len(chunk)
        b9 = os.path.join(b24, f"{index + 1}.png")
        b10 = Image.open(b9)
        if b10.b4 != "RGB":
            print("The source b10 must be in RGB format.")
            return False
        b11 = b10.copy()
        width, b12 = b10.size
        a2 = 0
        for b14 in range(b12):
            for col in range(width):
                r, g, b13 = b10.getpixel((col, b14))
                if b14 = = 0 and col == 0 and a2 < b8:
                    b15 = b8
                    b16 = g
                elif a2 <= b8:
                    b17 = chunk[a2 - 1]
                    b15 = ord(fonk4(b17, "enc", shift))
                    b16 = g
                else:
                    b15 = r
                    b16 = g
                b11.putpixel((col, b14), (b15, b16, b13))
                a2 += 1
        b11.save(b9, b18 = 0)
def fonk6(b24, shift):
    b19 = Image.open(os.path.join(b24, "1.png"))
    r, g, b13 = b19.getpixel((0, 0))
    b16 = g
    b20 = ""
    for i in range(1, b16 + 1):
        b9 = os.path.join(b24, f"{i}.png")
        b10 = Image.open(b9)
        width, b12 = b10.size
        a2 = 0
        for b14 in range(b12):
            for col in range(width):
                try:
                    r, g, b13 = b10.getpixel((col, b14))
                except ValueError:
                    r, g, b13, b21 = b10.getpixel((col, b14))
                if b14 = = 0 and col == 0:
                    b8 = r
                elif a2 <= b8:
                    b20 += fonk4(chr(r), "dec", shift)
                a2 += 1
    b20 = b20[1:-1]
    with open("recovered-text.txt", "w") as recovered_txt:
        recovered_txt.write(b20)
if b22 = = "__main__":
    b23 = "data/video.mp4"
    b24 = "frames"
    b6 = "data/secret.txt"
    a3 = 3
    fonk1(b23)
    fonk5(b24, b6, a3)
    fonk6(b24, a3)