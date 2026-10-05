
from aes import aes
key = "Thats my Kung Fu"
message = "Two One Nine Two"
encrypted_message = aes.encrypt(key, message)
print("Message:\t", message)
print("Encrypted:\t", encrypted_message)