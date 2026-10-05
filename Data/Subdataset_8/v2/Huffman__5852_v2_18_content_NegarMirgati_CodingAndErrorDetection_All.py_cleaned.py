import random
from Huffman import HuffmanCoding
from Convolutional import Convolutional
def noise(input_text):
    output = ''
    for bit in input_text:
        r = random.uniform(0, 1)
        if r < 0.1:
            output += str(1 - int(bit))
        else:
            output += bit
    return output
def main():
    huffman = HuffmanCoding()
    convolutional = Convolutional()
    input_text = "negarmirgati"
    print('Original input:', input_text)
    huffman_encoded = huffman.encode(input_text)
    print('Huffman coded:', huffman_encoded)
    convolutional_encoded = convolutional.encode(huffman_encoded)
    print('Convolutional encoded:', convolutional_encoded)
    input_with_noise = noise(convolutional_encoded)
    print('Noise added:', input_with_noise)
    convolutional_decoded = convolutional.decode(input_with_noise)
    print('Convolutional decoded:', convolutional_decoded)
    huffman_decoded = huffman.decode(convolutional_decoded)
    print('Huffman decoded:', huffman_decoded)
if __name__ == "__main__":
    main()