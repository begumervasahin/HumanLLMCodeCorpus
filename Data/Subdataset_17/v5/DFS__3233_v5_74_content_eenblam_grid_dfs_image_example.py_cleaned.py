from PIL import Image
def create_and_display_image():
    color_pattern = [
        (0, 0, 0),
        (0, 0, 0),
        (128, 128, 128),
        (255, 255, 255),
        (255, 255, 255)
    ]
    image_size = (100, 100)
    num_pixels = image_size[0] * image_size[1]
    pattern_length = len(color_pattern)
    repeated_pattern = color_pattern * (num_pixels
    image = Image.new("RGB", image_size, "white")
    image.putdata(repeated_pattern)
    image.show()
if __name__ == "__main__":
    create_and_display_image()