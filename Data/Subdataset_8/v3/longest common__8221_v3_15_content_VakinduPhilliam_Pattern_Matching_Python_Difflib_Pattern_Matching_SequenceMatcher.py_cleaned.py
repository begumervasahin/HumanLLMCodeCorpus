from difflib import SequenceMatcher
original_string = "private Thread currentThread;"
modified_string = "private volatile Thread currentThread;"
matcher = SequenceMatcher(lambda x: x == " ", original_string, modified_string)
similarity_ratio = round(matcher.ratio(), 3)
print("Similarity Ratio:", similarity_ratio)
print("Matching Blocks:")
for block in matcher.get_matching_blocks():
    a_start, b_start, length = block
    print(f"Match found at original[{a_start}] and modified[{b_start}] for {length} elements")
print("Operations to Transform:")
for opcode, a_start, a_end, b_start, b_end in matcher.get_opcodes():
    print(f"{opcode:6} original[{a_start}:{a_end}] -> modified[{b_start}:{b_end}]")