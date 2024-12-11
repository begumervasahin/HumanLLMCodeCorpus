from aes import aes
b1 = "Thats my Kung Fu"
b2 = "Two One Nine Two"
b3 = aes.encrypt(b1, b2)
print("Message:\t", b2)
print("Encrypted:\t", b3)