
from PIL import Image
def create_image():
    colors = [(0, 0, 0), (0, 0, 0), (128, 128, 128), (256, 256, 256), (256, 256, 256)]
    data = colors * 2000
    img = Image.new("RGB", (100, 100), "white")
    img.putdata(data)
    img.show()
if __name__ == "__main__":
    create_image()