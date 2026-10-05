from PIL import Image
import shutil
import cv2
import os
def fonk1(video_path):
    b1 = 'temp'
    try:
        os.makedirs(b1, b2 = True)
    except OSError:
        fonk2(b1)
        os.makedirs(b1)
    b3 = cv2.VideoCapture(video_path)
    a1 = 0
    while True:
        success, b4 = b3.read()
        if not success:
            break
        cv2.imwrite(os.path.join(b1, f"{a1}.png"), b4)
        a1 += 1
def fonk2(path):
    if os.path.exists(path):
        shutil.rmtree(path)
def fonk3(text, chunk_size):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
def fonk4(b17, b5, shift):
    if b5 = = "enc":
        return chr((ord(b17) + shift) % 128)
    elif b5 = = "dec":
        return chr((ord(b17) - shift) % 128)
def fonk5(frame_dir, text_to_hide_path, shift):
    with open(text_to_hide_path, "r") as file:
        b6 = repr(file.read())
    b7 = fonk3(b6, 255)
    for index, chunk in enumerate(b7):
        b8 = len(chunk)
        b9 = os.path.join(frame_dir, f"{index + 1}.png")
        b10 = Image.open(b9)
        if b10.b5 != "RGB":
            print("Source b10 must be in RGB format")
            return False
        b11 = b10.copy()
        width, b12 = b10.size
        a2 = 0
        for b14 in range(b12):
            for col in range(width):
                r, g, b13 = b10.getpixel((col, b14))
                if b14 = = 0 and col == 0 and a2 < b8:
                    b15 = b8
                    b16 = len(b7) if index == 0 else g
                elif a2 <= b8:
                    b17 = chunk[a2]
                    b15 = ord(fonk4(b17, "enc", shift))
                    b16 = g
                else:
                    b15 = r
                    b16 = g
                b11.putpixel((col, b14), (b15, b16, b13))
                a2 += 1
        b11.save(b9, b18 = 0)
def fonk6(frame_dir, shift):
    b19 = os.path.join(frame_dir, "1.png")
    b20 = Image.open(b19)
    r, g, b13 = b20.getpixel((0, 0))
    b16 = g
    b21 = ""
    for i in range(1, b16 + 1):
        b9 = os.path.join(frame_dir, f"{i}.png")
        b10 = Image.open(b9)
        width, b12 = b10.size
        a2 = 0
        for b14 in range(b12):
            for col in range(width):
                try:
                    r, g, b22 = b10.getpixel((col, b14))
                except ValueError:
                    r, g, b22, b22 = b10.getpixel((col, b14))
                if b14 = = 0 and col == 0:
                    b8 = r
                elif a2 <= b8:
                    b21 += fonk4(chr(r), "dec", shift)
                a2 += 1
    b21 = b21[1:-1]
    with open("data/recovered-text.txt", "w") as file:
        file.write(b21)
