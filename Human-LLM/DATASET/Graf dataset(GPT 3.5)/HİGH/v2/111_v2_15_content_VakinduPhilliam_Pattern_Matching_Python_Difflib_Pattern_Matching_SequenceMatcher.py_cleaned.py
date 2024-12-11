from difflib import SequenceMatcher
b1 = "private Thread currentThread;"
b2 = "private volatile Thread currentThread;"
b3 = SequenceMatcher(lambda x: x == " ", b1, b2)
b4 = round(b3.ratio(), 3)
print("Similarity Ratio:", b4)
print("Matching Blocks:")
for block in b3.get_matching_blocks():
    a_start, b_start, b5 = block
    print(f"a[{a_start}] and b[{b_start}] match for {b5} elements")
print("Operations to Transform:")
for operation in b3.get_opcodes():
    operation_type, a_start, a_end, b_start, b6 = operation
    print(f"{operation_type:6} a[{a_start}:{a_end}] b[{b_start}:{b6}]")