import random
from Huffman import HuffmanCoding
from Convolutional import Convolutional
def noise(input_str):
    output = ''
    for bit in input_str:
        random_prob = random.uniform(0, 1)
        if random_prob < 0.1:
            output += str(1 - int(bit))
        else:
            output += bit
    return output
def main():
    huffman_coder = HuffmanCoding()
    convolutional_coder = Convolutional()
    input_text = "negarmirgati"
    print('Input:', input_text)
    huffman_encoded = huffman_coder.encode(input_text)
    print('Huffman encoded:', huffman_encoded)
    convolutional_encoded = convolutional_coder.encode(huffman_encoded)
    print('Convolutional encoded:', convolutional_encoded)
    input_with_noise = noise(convolutional_encoded)
    print('Noise added:', input_with_noise)
    convolutional_decoded = convolutional_coder.decode(input_with_noise)
    print('Convolutional decoded:', convolutional_decoded)
    huffman_decoded = huffman_coder.decode(convolutional_decoded)
    print('Huffman decoded:', huffman_decoded)
if __name__ == "__main__":
    main()