import random
class HuffmanCoding:
    def encode(self, data):
        return ''.join(format(ord(char), '08b') for char in data)
    def decode(self, encoded_data):
        chars = [encoded_data[i:i + 8] for i in range(0, len(encoded_data), 8)]
        return ''.join(chr(int(char, 2)) for char in chars)
class Convolutional:
    def encode(self, data):
        return data
    def decode(self, encoded_data):
        return encoded_data
def noise(input_data):
    output = ''
    for i in range(len(input_data)):
        r = random.uniform(0, 1)
        if r < 0.1:
            output += str(1 - int(input_data[i]))
        else:
            output += input_data[i]
    return output
def main():
    h = HuffmanCoding()
    c = Convolutional()
    input_data = "negarmirgati"
    print('Input:', input_data)
    h_encoded = h.encode(input_data)
    print('Huffman encoded:', h_encoded)
    c_encoded = c.encode(h_encoded)
    print('Convolutional encoded:', c_encoded)
    input_with_noise = noise(c_encoded)
    print('Noise added:', input_with_noise)
    c_decoded = c.decode(input_with_noise)
    print('Convolutional decoded:', c_decoded)
    h_decoded = h.decode(c_decoded)
    print('Huffman decoded:', h_decoded)
if __name__ == "__main__":
    main()