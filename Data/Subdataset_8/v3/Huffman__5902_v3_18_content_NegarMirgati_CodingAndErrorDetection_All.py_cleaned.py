import random
from Huffman import HuffmanCoding
from Convolutional import Convolutional
def introduce_noise(input_text, noise_prob=0.1):
    output = ''
    for bit in input_text:
        if random.random() < noise_prob:
            output += str(1 - int(bit))
        else:
            output += bit
    return output
def main():
    huffman_coder = HuffmanCoding()
    convolutional_coder = Convolutional()
    original_input = "negarmirgati"
    print('Original input:', original_input)
    huffman_encoded = huffman_coder.encode(original_input)
    print('Huffman coded:', huffman_encoded)
    convolutional_encoded = convolutional_coder.encode(huffman_encoded)
    print('Convolutional encoded:', convolutional_encoded)
    noisy_input = introduce_noise(convolutional_encoded)
    print('Noise added:', noisy_input)
    convolutional_decoded = convolutional_coder.decode(noisy_input)
    print('Convolutional decoded:', convolutional_decoded)
    huffman_decoded = huffman_coder.decode(convolutional_decoded)
    print('Huffman decoded:', huffman_decoded)
if __name__ == "__main__":
    main()