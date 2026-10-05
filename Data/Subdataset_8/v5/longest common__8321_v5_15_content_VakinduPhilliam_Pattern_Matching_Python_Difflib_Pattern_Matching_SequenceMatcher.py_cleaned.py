from difflib import SequenceMatcher
string1 = "private Thread currentThread;"
string2 = "private volatile Thread currentThread;"
matcher = SequenceMatcher(lambda x: x == " ", string1, string2)
similarity_ratio = round(matcher.ratio(), 3)
print(f"Similarity ratio: {similarity_ratio}")
print("Matching blocks:")
for block in matcher.get_matching_blocks():
    a_start, b_start, length = block
    print(f"  Common elements from index {a_start} in string1 and {b_start} in string2: {length}")
print("Operations:")
for opcode, a_start, a_end, b_start, b_end in matcher.get_opcodes():
    print(f"  Operation: {opcode}, Elements from string1[{a_start}:{a_end}] and string2[{b_start}:{b_end}]")