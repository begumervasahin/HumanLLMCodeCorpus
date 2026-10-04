import random
from Huffman import HuffmanCoding
from Convolutional import Convolutional
def add_noise(encoded_data, noise_level=0.1):
    noisy_output = ''
    for bit in encoded_data:
        if random.uniform(0, 1) < noise_level:
            noisy_output += str(1 - int(bit))
        else:
            noisy_output += bit
    return noisy_output
def main():
    huffman = HuffmanCoding()
    convolutional = Convolutional()
    input_string = "negarmirgati"
    print('Input:', input_string)
    huffman_encoded = huffman.encode(input_string)
    print('Huffman Encoded:', huffman_encoded)
    convolutional_encoded = convolutional.encode(huffman_encoded)
    print('Convolutional Encoded:', convolutional_encoded)
    noisy_input = add_noise(convolutional_encoded)
    print('Noisy Input:', noisy_input)
    convolutional_decoded = convolutional.decode(noisy_input)
    print('Convolutional Decoded:', convolutional_decoded)
    huffman_decoded = huffman.decode(convolutional_decoded)
    print('Huffman Decoded:', huffman_decoded)
if __name__ == "__main__":
    main()