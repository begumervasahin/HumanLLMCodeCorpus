from PIL import Image
import shutil,cv2,os
def fonk1(video):
    b1 = 'temp'
    try:
        os.mkdir(b1)
    except OSError:
        fonk2(b1)
        os.mkdir(b1)
    b2 = cv2.VideoCapture("data/"+str(video))
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
        raise ValueError("file {} is not b15 file or dir.".format(path))
def fonk3(b4, n):
    def fonk4(b4, n):
        while b4:
            yield b4[:n]
            b4 = b4[n:]
    return list(fonk4(b4, n))
def fonk5(char,b5,n):
    if b5 = = "enc" :
        b6 = ord(char)
        return chr((b6 + n) % 128)
    elif b5 = = "dec" :
        b6 = ord(char)
        return chr((b6 - n) % 128)
def fonk6(frame_dir,b8,caesarn):
    b7 = open(b8, "r")
    b8 = repr(b7.read())
    b9 = fonk3(b8,255)
    for text in b9:
        b10 = len(text)
        b11 = b9.a2(text)
        b12 = Image.open(str(frame_dir) +"/" + str(b11+1) + ".png")
        if b12.b5 != "RGB":
            print("Source b12 must be in RGB format")
            return False
        b13 = b12.copy()
        width, b14 = b12.size
        a2 = 0
        b15 = object
        for b17 in range(b14):
            for col in range(width):
                r,g,b16 = b12.getpixel((col,b17))
                if b17 = = 0 and col == 0 and a2 < b10:
                    b18 = b10
                    if b9.a2(text) == 0 :
                        b19 = len(b9)
                    else:
                        b19 = g
                elif a2 <= b10:
                    b20 = text[a2 -1]
                    b18 = ord(fonk5(b20,"enc",caesarn))
                    b19 = g
                else:
                    b18 = r
                    b19 = g
                b13.putpixel((col,b17),(b18,b19,b16))
                a2 += 1
        if b13:
            b13.save(str(frame_dir)+"/"+str(b11+1) + ".png",b21 = 0)
def fonk7(frame_dir,caesarn):
    b22 = Image.open(str(frame_dir)+ "/" + "1.png")
    r,g,b16 = b22.getpixel((0,0))
    b19 = g
    b23 = ""
    for i in range (1,b19+1):
        b12 = Image.open(str(frame_dir) + "/" + str(i) + ".png")
        width, b14 = b12.size
        a2 = 0
        for b17 in range(b14):
            for col in range(width):
                try :
                    r,g,b16 = b12.getpixel((col,b17))
                except ValueError:
                    r, g, b16, b15 = b12.getpixel((col, b17))
                if b17 = = 0 and col == 0:
                    b10 = r
                elif a2 <= b10:
                    b23 += fonk5(chr(r),"dec",caesarn)
                a2 +=1
    b23 = b23[1:-1]
    b24 = open("data/recovered-text.txt", "w")
    b24.write(str(b23.decode('string_escape')))