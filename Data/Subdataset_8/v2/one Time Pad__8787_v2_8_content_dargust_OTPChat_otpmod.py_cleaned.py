import _pickle as cPickle
import string
import secrets
class OneTimePad:
    DEFAULT_ALPHABET = string.digits + string.ascii_letters + string.punctuation + " "
    DEFAULT_MESSAGE_LENGTH = 64
    DEFAULT_KEY_NUMBER = 0xffff
    DEFAULT_FILE = "key.dict"
    def __init__(self, alphabet=None, message_length=None, key_number=None, file=None, outqueue=None):
        self.alphabet = alphabet or self.DEFAULT_ALPHABET
        self.message_length = message_length or self.DEFAULT_MESSAGE_LENGTH
        self.max_keys = key_number or self.DEFAULT_KEY_NUMBER
        self.file = file or self.DEFAULT_FILE
        if outqueue:
            outqueue.put("Starting")
        self.secure_random = secrets.SystemRandom()
        try:
            with open(self.file, 'rb') as f:
                self.key_dict = cPickle.load(f)
                print("Loaded settings from file")
                settings = self.key_dict[0]
                self.alphabet = settings[0]
                self.message_length = settings[1]
                self.max_keys = settings[2]
        except FileNotFoundError:
            self.generate_keys(outqueue)
        print("Keys remaining: {}".format(len(self.key_dict) - 1))
        if outqueue:
            outqueue.put("Stopped")
    def generate_keys(self, outqueue):
        print("Generating new key dictionary with {} keys".format(self.max_keys))
        print("This may take a few minutes")
        keys = {}
        last_prog = 0
        keys[0] = (self.alphabet, self.message_length, self.max_keys)
        for i in range(self.max_keys):
            keys[i + 1] = "".join(self.secure_random.choice(self.alphabet) for _ in range(self.message_length))
            if i % int(self.max_keys / 100) == 0:
                prog = int(i / (self.max_keys / 100))
                if prog != last_prog and outqueue:
                    outqueue.put("Step")
                    last_prog = prog
        with open(self.file, 'wb') as f:
            cPickle.dump(keys, f, -1)
        self.key_dict = keys
        print("Finished")
    def get_key_len(self, x):
        return len(hex(x)) - 2
    def encode(self, message):
        try:
            keyprefix = self.get_key_len(self.max_keys)
            prefix, key = self.secure_random.choice(list(self.key_dict.items())[1:])
            self.key_dict.pop(prefix)
            with open(self.file, 'wb') as f:
                cPickle.dump(self.key_dict, f, -1)
            prefix = "{0:0{1}x}".format(prefix, keyprefix)
            message = message.ljust(self.message_length)
            if len(message) > self.message_length:
                raise ValueError("Message length greater than {}".format(self.message_length))
            encoded_message = prefix + ''.join(self.alphabet[(self.alphabet.index(message[i]) + self.alphabet.index(key[i])) % len(self.alphabet)] for i in range(self.message_length))
            return encoded_message, True
        except KeyError as err:
            return "Unable to encode message: {}".format(err), False
        except ValueError as err:
            return "Unable to encode message: {}".format(err), False
    def decode(self, encoded_data):
        keyprefix = self.get_key_len(self.max_keys)
        try:
            key = self.key_dict[int(encoded_data[:keyprefix], 16)]
            self.key_dict.pop(int(encoded_data[:keyprefix], 16))
            with open(self.file, 'wb') as f:
                cPickle.dump(self.key_dict, f, -1)
            encoded_data = encoded_data[keyprefix:]
            return ''.join(self.alphabet[(self.alphabet.index(encoded_data[i]) - self.alphabet.index(key[i])) % len(self.alphabet)] for i in range(self.message_length))
        except KeyError:
            return "Unable to decode data"
if __name__ == "__main__":
    otp = OneTimePad()
    message = "Hello, World!"
    encoded_message, _ = otp.encode(message)
    print("Encoded message:", encoded_message)
    decoded_message = otp.decode(encoded_message)
    print("Decoded message:", decoded_message)