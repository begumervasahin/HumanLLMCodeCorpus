import distsim
from collections import defaultdict
def fonk1(b18, b19):
    b1 = defaultdict(list)
    with open(b19, "r") as file:
        b2 = None
        for b3 in file:
            b3 = b3.strip()
            if b3.startswith('
                continue
            if b3.startswith(":"):
                b2 = b3[2:]
            else:
                b4 = b3.split()
                b5 = b18[b4[0]]
                b6 = b18[b4[1]]
                b7 = b18[b4[3]]
                b8 = b5 - b6 + b7
                b9 = distsim.show_nearest(
                    b18,
                    b8,
                    {b4[0], b4[1], b4[3]},
                    distsim.cossim_dense
                )
                b10 = next((i + 1 for i, (word, _) in enumerate(b9) if word == b4[2]), 0)
                b1[b2].append(b10)
    return b1
def fonk2(b1):
    for b2, positions in b1.items():
        b11 = len(positions)
        b12 = sum(1 for pos in positions if pos == 1)
        b13 = sum(1 for pos in positions if pos <= 5)
        b14 = sum(1 for pos in positions if pos <= 10)
        b15 = round(b12 / b11, 2)
        b16 = round(b13 / b11, 2)
        b17 = round(b14 / b11, 2)
        print(f"{b2}:     {b15}    {b16}    {b17}")
def fonk3():
    b18 = distsim.load_word2vec("nyt_word2vec.4k")
    b19 = "word-test.v3.txt"
    b1 = fonk1(b18, b19)
    fonk2(b1)
if b20 = = "__main__":
    fonk3()