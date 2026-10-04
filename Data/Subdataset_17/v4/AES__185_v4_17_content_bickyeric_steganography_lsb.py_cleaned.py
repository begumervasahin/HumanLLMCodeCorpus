import cv2
class AppError(Exception):
    pass
def int_to_bin(i, length):
    binary = bin(i)[2:]
    if len(binary) > length:
        raise AppError("Bit size is larger than expected.")
    return binary.zfill(length)
def char_to_bin(c):
    return int_to_bin(ord(c), 8)
class LSB:
    MAX_BIT_LENGTH = 16
    def __init__(self, img):
        self.size_x, self.size_y, self.size_channel = img.shape
        self.image = img
        self.cur_x = 0
        self.cur_y = 0
        self.cur_channel = 0
    def next_pixel(self):
        if self.cur_channel < self.size_channel - 1:
            self.cur_channel += 1
        else:
            self.cur_channel = 0
            if self.cur_y < self.size_y - 1:
                self.cur_y += 1
            else:
                self.cur_y = 0
                if self.cur_x < self.size_x - 1:
                    self.cur_x += 1
                else:
                    raise AppError("Need a larger image.")
    def put_bit(self, bit):
        v = self.image[self.cur_x, self.cur_y][self.cur_channel]
        binary_v = bin(v)[2:].zfill(8)
        if binary_v[-1] != bit:
            binary_v = binary_v[:-1] + bit
        self.image[self.cur_x, self.cur_y][self.cur_channel] = int(binary_v, 2)
        self.next_pixel()
    def put_bits(self, bits):
        for bit in bits:
            self.put_bit(bit)
    def read_bit(self):
        v = self.image[self.cur_x, self.cur_y][self.cur_channel]
        return bin(v)[-1]
    def read_bits(self, length):
        bits = ""
        for _ in range(length):
            bits += self.read_bit()
            self.next_pixel()
        return bits
    def embed(self, text):
        text_length = int_to_bin(len(text), self.MAX_BIT_LENGTH)
        self.put_bits(text_length)
        for char in text:
            bits = char_to_bin(char)
            self.put_bits(bits)
    def extract(self):
        length = int(self.read_bits(self.MAX_BIT_LENGTH), 2)
        text = ""
        for _ in range(length):
            char = int(self.read_bits(8), 2)
            text += chr(char)
        return text
    def save(self, dst_path):
        cv2.imwrite(dst_path, self.image)
if __name__ == "__main__":
    image_path = 'dst.png'
    output_path = 'output.png'
    text_to_embed = "Hidden Message"
    img = cv2.imread(image_path)
    if img is None:
        raise AppError(f"Image not found at path: {image_path}")
    lsb = LSB(img)
    lsb.embed(text_to_embed)
    lsb.save(output_path)
    img = cv2.imread(output_path)
    if img is None:
        raise AppError(f"Image not found at path: {output_path}")
    lsb = LSB(img)
    extracted_text = lsb.extract()
    print("Extracted text:", extracted_text)