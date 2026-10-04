import distsim
from collections import defaultdict
def fonk1():
    b1 = distsim.load_word2vec("nyt_word2vec.4k")
    b2 = defaultdict(list)
    with open("b12-test.v3.txt", "r") as file:
        b3 = None
        for b4 in file:
            b4 = b4.strip('\n')
            if b4.startswith('
                continue
            if b4.startswith(":"):
                b3 = b4[2:]
            else:
                b5 = b4.split()
                b6 = b1[b5[0]]
                b7 = b1[b5[1]]
                b8 = b1[b5[3]]
                b9 = b6 - b7 + b8
                b10 = distsim.show_nearest(b1, b9, {b5[0], b5[1], b5[3]}, distsim.cossim_dense)
                b11 = False
                for a1, (b12, score) in enumerate(b10):
                    if b12 = = b5[2]:
                        b11 = True
                        break
                if not b11:
                    a1 = 0
                else:
                    a1 += 1
                b2[b3].append(a1)
    for b3, positions in b2.items():
        b13 = sum(1 for pos in positions if pos == 1)
        b14 = sum(1 for pos in positions if pos <= 5)
        b15 = sum(1 for pos in positions if pos <= 10)
        b16 = len(positions)
        b17 = round(float(b13) / b16, 2)
        b18 = round(float(b14) / b16, 2)
        b19 = round(float(b15) / b16, 2)
        print(f"{b3}:     {b17}    {b18}    {b19}")
if b20 = = "__main__":
    fonk1()