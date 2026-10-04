from difflib import SequenceMatcher
def fonk1():
    b1 = "private Thread currentThread;"
    b2 = "private volatile Thread currentThread;"
    b3 = SequenceMatcher(lambda x: x == " ", b1, b2)
    b4 = round(b3.ratio(), 3)
    print(f"Similarity ratio: {b4}")
    print("\nMatching blocks:")
    for block in b3.get_matching_blocks():
        a_index, b_index, b5 = block
        print(f"a[{a_index}] and b[{b_index}] match for {b5} elements")
    print("\nOpcodes:")
    for opcode in b3.get_opcodes():
        tag, i1, i2, j1, b6 = opcode
        print(f"{tag.capitalize():>7} a[{i1}:{i2}] b[{j1}:{b6}]")
if b7 = = "__main__":
    fonk1()