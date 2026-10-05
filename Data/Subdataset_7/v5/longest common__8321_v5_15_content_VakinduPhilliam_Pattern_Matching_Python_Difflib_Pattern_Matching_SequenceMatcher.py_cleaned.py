from difflib import SequenceMatcher
b1 = "private Thread currentThread;"
b2 = "private volatile Thread currentThread;"
b3 = SequenceMatcher(lambda x: x == " ", b1, b2)
b4 = round(b3.ratio(), 3)
print(f"Similarity ratio: {b4}")
print("Matching blocks:")
for block in b3.get_matching_blocks():
    a_start, b_start, b5 = block
    print(f"  Common elements from index {a_start} in b1 and {b_start} in b2: {b5}")
print("Operations:")
for opcode, a_start, a_end, b_start, b_end in b3.get_opcodes():
    print(f"  Operation: {opcode}, Elements from b1[{a_start}:{a_end}] and b2[{b_start}:{b_end}]")