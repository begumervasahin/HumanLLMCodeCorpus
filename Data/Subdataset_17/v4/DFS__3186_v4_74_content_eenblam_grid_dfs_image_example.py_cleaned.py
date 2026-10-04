from PIL import Image
def create_and_display_image():
    color_pattern = [
        (0, 0, 0),
        (0, 0, 0),
        (128, 128, 128),
        (255, 255, 255),
        (255, 255, 255)
    ]
    num_pixels = 100 * 100
    repeated_pattern = color_pattern * (num_pixels
    image = Image.new("RGB", (100, 100), "white")
    image.putdata(repeated_pattern)
    image.show()
if __name__ == "__main__":
    create_and_display_image()