import cv2
class AppError(BaseException):
    pass
def int_to_binary(i, length):
    binary = bin(i)[2:]
    if len(binary) > length:
        raise AppError("Bit size is larger than expected.")
    return binary.zfill(length)
def char_to_binary(c):
    return int_to_binary(ord(c), 8)
class LSB:
    MAX_BIT_LENGTH = 16
    def __init__(self, image):
        self.image = image
        self.size_x, self.size_y, self.size_channel = image.shape
        self.cur_x, self.cur_y, self.cur_channel = 0, 0, 0
    def move_to_next_pixel(self):
        self.cur_channel = (self.cur_channel + 1) % self.size_channel
        if self.cur_channel == 0:
            self.cur_y = (self.cur_y + 1) % self.size_y
            if self.cur_y == 0:
                self.cur_x = (self.cur_x + 1) % self.size_x
                if self.cur_x == 0:
                    raise AppError("Need larger image")
    def embed_bit(self, bit):
        pixel_value = self.image[self.cur_x, self.cur_y][self.cur_channel]
        binary_pixel_value = bin(pixel_value)[2:].zfill(8)
        binary_pixel_value = binary_pixel_value[:-1] + bit
        self.image[self.cur_x, self.cur_y][self.cur_channel] = int(binary_pixel_value, 2)
        self.move_to_next_pixel()
    def embed_bits(self, bits):
        for bit in bits:
            self.embed_bit(bit)
    def read_bit(self):
        pixel_value = self.image[self.cur_x, self.cur_y][self.cur_channel]
        return bin(pixel_value)[-1]
    def read_bits(self, length):
        bits = ""
        for _ in range(length):
            bits += self.read_bit()
            self.move_to_next_pixel()
        return bits
    def embed_text(self, text):
        text_length_binary = int_to_binary(len(text), self.MAX_BIT_LENGTH)
        self.embed_bits(text_length_binary)
        for c in text:
            char_bits = char_to_binary(c)
            self.embed_bits(char_bits)
    def extract_text(self):
        text_length = int(self.read_bits(self.MAX_BIT_LENGTH), 2)
        text = ""
        for _ in range(text_length):
            char_value = int(self.read_bits(8), 2)
            text += chr(char_value)
        return text
    def save_image(self, dst_path):
        cv2.imwrite(dst_path, self.image)
if __name__ == "__main__":
    lsb = LSB(cv2.imread('dst.png'))
    extracted_text = lsb.extract_text()
    print(extracted_text)