import random
class HuffmanCoding:
    def encode(self, data):
        return ''.join(format(ord(char), '08b') for char in data)
    def decode(self, encoded_data):
        return ''.join(chr(int(encoded_data[i:i + 8], 2)) for i in range(0, len(encoded_data), 8))
class ConvolutionalCoding:
    def encode(self, data):
        return data
    def decode(self, encoded_data):
        return encoded_data
def introduce_noise(data, noise_probability=0.1):
    return ''.join(
        str(1 - int(bit)) if random.uniform(0, 1) < noise_probability else bit
        for bit in data
    )
def main():
    huffman = HuffmanCoding()
    convolutional = ConvolutionalCoding()
    input_data = "negarmirgati"
    print('Input:', input_data)
    huffman_encoded = huffman.encode(input_data)
    print('Huffman encoded:', huffman_encoded)
    convolutional_encoded = convolutional.encode(huffman_encoded)
    print('Convolutional encoded:', convolutional_encoded)
    noisy_data = introduce_noise(convolutional_encoded)
    print('Noisy data:', noisy_data)
    convolutional_decoded = convolutional.decode(noisy_data)
    print('Convolutional decoded:', convolutional_decoded)
    huffman_decoded = huffman.decode(convolutional_decoded)
    print('Huffman decoded:', huffman_decoded)
if __name__ == "__main__":
    main()