from PIL import Image
b1 = [(0,0,0), (0,0,0), (128,128,128), (256,256,256), (256,256,256)] * 2000
b2 = Image.new("RGB", (100,100), "white")
b2.putdata(b1)
b2.show()