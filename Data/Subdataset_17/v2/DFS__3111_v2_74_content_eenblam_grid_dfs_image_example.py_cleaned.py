from PIL import Image
def create_image():
    color_pattern = [
        (0, 0, 0),
        (0, 0, 0),
        (128, 128, 128),
        (255, 255, 255),
        (255, 255, 255)
    ]
    pattern_length = len(color_pattern)
    data = color_pattern * (100 * 100
    image_size = (100, 100)
    image = Image.new("RGB", image_size, "white")
    image.putdata(data)
    image.show()
if __name__ == "__main__":
    create_image()