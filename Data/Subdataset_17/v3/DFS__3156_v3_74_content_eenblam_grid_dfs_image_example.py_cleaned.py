from PIL import Image
def create_image():
    color_pattern = [
        (0, 0, 0),
        (0, 0, 0),
        (128, 128, 128),
        (255, 255, 255),
        (255, 255, 255)
    ]
    num_pixels = 100 * 100
    data = (color_pattern * (num_pixels
    image = Image.new("RGB", (100, 100), "white")
    image.putdata(data)
    image.show()
if __name__ == "__main__":
    create_image()