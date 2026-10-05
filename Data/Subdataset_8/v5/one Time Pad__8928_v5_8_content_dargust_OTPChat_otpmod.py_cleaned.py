import _pickle as cPickle
import string
import secrets
class OTP:
    def __init__(self, alphabet=None, message_length=None, key_number=None, file=None, outqueue=None):
        self.defaults_alphabet = string.digits + string.ascii_letters + string.punctuation + " "
        self.defaults_message_length = 64
        self.defaults_key_number = 0xffff
        self.defaults_file = "key.dict"
        self.alphabet = alphabet if alphabet else self.defaults_alphabet
        self.message_length = message_length if message_length else self.defaults_message_length
        self.MAX_KEYS = key_number if key_number else self.defaults_key_number
        self.file = file if file else self.defaults_file
        if outqueue:
            outqueue.put("Starting")
        self.secure_random = secrets.SystemRandom()
        try:
            with open(self.file, 'rb') as f:
                self.key_dict = cPickle.load(f)
                print("Loaded dictionary settings from file")
                self._load_settings()
        except FileNotFoundError:
            self._generate_key_dict(outqueue)
        print("Keys remaining: {}".format(len(self.key_dict) - 1))
        if outqueue:
            outqueue.put("Stopped")
    def _load_settings(self):
        settings = self.key_dict[0]
        self.alphabet, self.message_length, self.MAX_KEYS = settings
    def _generate_key_dict(self, outqueue):
        print("Generating a new key dictionary with {} keys".format(self.MAX_KEYS))
        print("This may take a few minutes")
        self.key_dict = {0: (self.alphabet, self.message_length, self.MAX_KEYS)}
        last_prog = 0
        for i in range(self.MAX_KEYS):
            key = "".join(self.secure_random.choice(self.alphabet) for _ in range(self.message_length))
            self.key_dict[i + 1] = key
            if i % int(self.MAX_KEYS / 100) == 0:
                prog = int(i / (self.MAX_KEYS / 100))
                if prog != last_prog and outqueue:
                    outqueue.put("Step")
                    last_prog = prog
        with open(self.file, 'wb') as f:
            cPickle.dump(self.key_dict, f, -1)
        print("Key dictionary generation complete")
    def _get_key_prefix_length(self):
        return len(hex(self.MAX_KEYS)) - 2
    def encode(self, message):
        try:
            key_prefix_len = self._get_key_prefix_length()
            prefix, key = self.secure_random.choice(list(self.key_dict.items())[1:])
            self.key_dict.pop(prefix)
            with open(self.file, 'wb') as f:
                cPickle.dump(self.key_dict, f, -1)
            prefix = "{0:0{1}x}".format(prefix, key_prefix_len)
            message = message.ljust(self.message_length)
            if len(message) > self.message_length:
                raise ValueError("Message length exceeds {}".format(self.message_length))
            encoded_message = prefix + ''.join(self.alphabet[(self.alphabet.index(message[i]) + self.alphabet.index(key[i])) % len(self.alphabet)] for i in range(self.message_length))
            return encoded_message, True
        except (KeyError, ValueError) as err:
            return "Unable to encode message: {}".format(err), False
    def decode(self, data):
        key_prefix_len = self._get_key_prefix_length()
        try:
            key = self.key_dict[int(data[:key_prefix_len], 16)]
            self.key_dict.pop(int(data[:key_prefix_len], 16))
            with open(self.file, 'wb') as f:
                cPickle.dump(self.key_dict, f, -1)
            data = data[key_prefix_len:]
            return ''.join(self.alphabet[(self.alphabet.index(data[i]) - self.alphabet.index(key[i])) % len(self.alphabet)] for i in range(self.message_length))
        except KeyError:
            return "Unable to decode data"