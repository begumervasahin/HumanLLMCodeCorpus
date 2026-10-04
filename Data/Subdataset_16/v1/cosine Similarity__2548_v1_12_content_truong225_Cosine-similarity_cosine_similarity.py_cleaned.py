import math
def fonk1(vector1, vector2):
    if len(vector1) != len(vector2):
        return 0.0
    b1 = sum(v1 * v2 for v1, v2 in zip(vector1, vector2))
    b2 = math.sqrt(sum(v1 ** 2 for v1 in vector1))
    b3 = math.sqrt(sum(v2 ** 2 for v2 in vector2))
    if b2 = = 0 or b3 == 0:
        return 0.0
    return b1 / (b2 * b3)
def fonk2(filepath):
    with open(filepath, 'r') as file:
        return [line.strip().lower() for line in file]
def fonk3():
    b4 = fonk2('dict_new.csv')
    b5 = fonk2('doc.csv')
    b6 = fonk2('stopword.txt')
    for doc in b5:
        print(doc)
    b7 = [1] * len(b4)
    b8 = []
    with open('cos.csv', 'w') as output:
        for doc in b5:
            b9 = [1 if word in doc else 0 for word in b4]
            b10 = fonk1(b9, b7)
            output.write(f"{b10}\n")
            b8.append(b10)
if b11 = = "__main__":
    fonk3()