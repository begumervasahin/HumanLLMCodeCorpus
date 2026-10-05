import argparse
def fonk1():
    b1 = []
    b2 = int(input("Enter the number of ciphertexts: "))
    for _ in range(b2):
        b1.append(input("Enter the ciphertext: "))
    return b1
def fonk2(b1):
    b3 = ['*' * (len(ciphertext)
    return b3
def fonk3(text_index1, text_index2, b3):
    for i in range(len(b3[text_index1])):
        if b3[text_index1][i] != '*' and b3[text_index2][i] != '*' and b3[text_index1][i] != b3[text_index2][i]:
            b3[text_index1] = b3[text_index1][:i] + '*' + b3[text_index1][i+1:]
            b3[text_index2] = b3[text_index2][:i] + '*' + b3[text_index2][i+1:]
def fonk4():
    b4 = argparse.ArgumentParser(description='Process argument full.')
    b4.add_argument('--full', b5 = int, help='whether display all possible characters or not, default is 0')
    b6 = b4.parse_args()
    b7 = b6.full if b6.full is not None else 0
    b1 = fonk1()
    b3 = fonk2(b1)
    if len(b1) < 2:
        raise Exception("One-time pad is secure if only one ciphertext is observed!")
    for i in range(len(b1)):
        for j in range(i + 1, len(b1)):
            fonk3(i, j, b3)
    print("Plaintext possibilities:")
    for i, plaintext in enumerate(b3):
        print(f"Ciphertext {i + 1}: {plaintext}")
if b8 = = "__main__":
    fonk4()