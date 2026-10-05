import pickle
import sys
class CipherStructure:
    def __init__(self, ciphered_text, key, initialization_vector, tag_sentence, signature):
        self.ciphered_text = ciphered_text
        self.key = key
        self.initialization_vector = initialization_vector
        self.tag_sentence = tag_sentence
        self.signature = signature
    def get_ciphered_text(self):
        return self.ciphered_text
    def get_key(self):
        return self.key
    def get_initialization_vector(self):
        return self.initialization_vector
    def get_tag_sentence(self):
        return self.tag_sentence
    def get_signature(self):
        return self.signature
    def dump_to_file(self, output_file):
        with open(output_file, 'wb') as file:
            pickle.dump(self, file)
    @staticmethod
    def load_from_file(input_file):
        try:
            with open(input_file, 'rb') as file:
                obj = pickle.load(file)
                if isinstance(obj, CipherStructure):
                    return obj
        except Exception as e:
            print("Error occurred while loading from file:", e)
            sys.exit()
def main():
    cipher = CipherStructure("ciphered_text", "key", "initialization_vector", "tag_sentence", "signature")
    cipher.dump_to_file("cipher_file.pickle")
    loaded_cipher = CipherStructure.load_from_file("cipher_file.pickle")
    print("Loaded ciphered_text:", loaded_cipher.get_ciphered_text())
    print("Loaded key:", loaded_cipher.get_key())
    print("Loaded initialization_vector:", loaded_cipher.get_initialization_vector())
    print("Loaded tag_sentence:", loaded_cipher.get_tag_sentence())
    print("Loaded signature:", loaded_cipher.get_signature())
if __name__ == "__main__":
    main()