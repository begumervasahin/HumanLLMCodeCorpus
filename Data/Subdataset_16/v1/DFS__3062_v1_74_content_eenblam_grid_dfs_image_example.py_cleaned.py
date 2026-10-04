
from PIL import Image
def fonk1():
    b1 = [(0, 0, 0), (0, 0, 0), (128, 128, 128), (256, 256, 256), (256, 256, 256)]
    b2 = b1 * 2000
    b3 = Image.new("RGB", (100, 100), "white")
    b3.putdata(b2)
    b3.show()
if b4 = = "__main__":
    fonk1()