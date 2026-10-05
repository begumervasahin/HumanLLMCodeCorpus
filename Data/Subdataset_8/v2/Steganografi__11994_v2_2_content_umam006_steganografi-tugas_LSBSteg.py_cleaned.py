import cv2
import numpy as np
import argparse
class SteganographyException(Exception):
    pass
class LSBSteg:
    def __init__(self, im):
        self.image = im
        self.height, self.width, self.nbchannels = im.shape
        self.size = self.width * self.height
        self.maskONEValues = [1, 2, 4, 8, 16, 32, 64, 128]
        self.maskZEROValues = [254, 253, 251, 247, 239, 223, 191, 127]
        self.curwidth = 0
        self.curheight = 0
        self.curchan = 0
        self.maskONE = self.maskONEValues.pop(0)
        self.maskZERO = self.maskZEROValues.pop(0)
    def put_binary_value(self, bits):
        for bit in bits:
            pixel_value = list(self.image[self.curheight, self.curwidth])
            if int(bit) == 1:
                pixel_value[self.curchan] |= self.maskONE
            else:
                pixel_value[self.curchan] &= self.maskZERO
            self.image[self.curheight, self.curwidth] = tuple(pixel_value)
            self._move_to_next_slot()
    def _move_to_next_slot(self):
        if self.curchan == self.nbchannels - 1:
            self.curchan = 0
            if self.curwidth == self.width - 1:
                self.curwidth = 0
                if self.curheight == self.height - 1:
                    self.curheight = 0
                    if self.maskONE == 128:
                        raise SteganographyException("No available slot remaining (image filled)")
                    else:
                        self.maskONE = self.maskONEValues.pop(0)
                        self.maskZERO = self.maskZEROValues.pop(0)
                else:
                    self.curheight += 1
            else:
                self.curwidth += 1
        else:
            self.curchan += 1
    def read_bit(self):
        pixel_value = self.image[self.curheight, self.curwidth][self.curchan]
        bit_value = int(pixel_value) & self.maskONE
        self._move_to_next_slot()
        return "1" if bit_value > 0 else "0"
    def read_byte(self):
        return self.read_bits(8)
    def read_bits(self, nb):
        bits = ""
        for _ in range(nb):
            bits += self.read_bit()
        return bits
    def encode_text(self, txt):
        txt_length = len(txt)
        txt_length_bin = bin(txt_length)[2:].zfill(16)
        self.put_binary_value(txt_length_bin)
        for char in txt:
            char_bin = bin(ord(char))[2:].zfill(8)
            self.put_binary_value(char_bin)
        return self.image
    def decode_text(self):
        txt_length_bin = self.read_bits(16)
        txt_length = int(txt_length_bin, 2)
        decoded_text = ""
        for _ in range(txt_length):
            char_bin = self.read_byte()
            decoded_text += chr(int(char_bin, 2))
        return decoded_text
    def encode_image(self, imtohide):
        emb_height, emb_width, emb_channels = imtohide.shape
        if self.width * self.height * self.nbchannels < emb_width * emb_height * emb_channels:
            raise SteganographyException("Carrier image not big enough to hold all the data for steganography")
        self.put_binary_value(bin(emb_width)[2:].zfill(16))
        self.put_binary_value(bin(emb_height)[2:].zfill(16))
        for i in range(emb_height):
            for j in range(emb_width):
                for chan in range(emb_channels):
                    val_bin = bin(imtohide[i, j][chan])[2:].zfill(8)
                    self.put_binary_value(val_bin)
        return self.image
    def decode_image(self):
        emb_width = int(self.read_bits(16), 2)
        emb_height = int(self.read_bits(16), 2)
        extracted_image = np.zeros((emb_height, emb_width, 3), np.uint8)
        for i in range(emb_height):
            for j in range(emb_width):
                for chan in range(extracted_image.shape[2]):
                    pixel_value_bin = self.read_byte()
                    extracted_image[i, j][chan] = int(pixel_value_bin, 2)
        return extracted_image
    def encode_binary(self, data):
        data_length = len(data)
        if self.width * self.height * self.nbchannels < data_length + 64:
            raise SteganographyException("Carrier image not big enough to hold all the data for steganography")
        self.put_binary_value(bin(data_length)[2:].zfill(64))
        for byte in data:
            byte_bin = bin(byte)[2:].zfill(8)
            self.put_binary_value(byte_bin)
        return self.image
    def decode_binary(self):
        data_length_bin = self.read_bits(64)
        data_length = int(data_length_bin, 2)