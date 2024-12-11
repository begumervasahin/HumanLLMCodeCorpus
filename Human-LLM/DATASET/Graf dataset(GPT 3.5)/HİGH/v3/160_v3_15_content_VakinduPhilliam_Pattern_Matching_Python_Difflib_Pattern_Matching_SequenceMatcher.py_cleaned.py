from difflib import SequenceMatcher
b1 = "private Thread currentThread;"
b2 = "private volatile Thread currentThread;"
b3 = SequenceMatcher(lambda x: x == " ", b1, b2)
b4 = round(b3.ratio(), 3)
print("Similarity Ratio:", b4)
print("Matching Blocks:")
for block in b3.get_matching_blocks():
    a_start, b_start, b5 = block
    print(f"Match found at original[{a_start}] and modified[{b_start}] for {b5} elements")
print("Operations to Transform:")
for opcode, a_start, a_end, b_start, b_end in b3.get_opcodes():
    print(f"{opcode:6} original[{a_start}:{a_end}] -> modified[{b_start}:{b_end}]")