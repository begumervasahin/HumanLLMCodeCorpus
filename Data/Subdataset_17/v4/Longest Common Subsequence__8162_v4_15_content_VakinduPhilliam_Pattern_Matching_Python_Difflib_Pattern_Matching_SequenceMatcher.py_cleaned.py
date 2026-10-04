from difflib import SequenceMatcher
string_a = "private Thread currentThread;"
string_b = "private volatile Thread currentThread;"
s = SequenceMatcher(lambda x: x == " ", string_a, string_b)
similarity_ratio = round(s.ratio(), 3)
print(similarity_ratio)
for block in s.get_matching_blocks():
    print(f"a[{block[0]}] and b[{block[1]}] match for {block[2]} elements")
for opcode in s.get_opcodes():
    print(f"{opcode[0]:>6} a[{opcode[1]}:{opcode[2]}] b[{opcode[3]}:{opcode[4]}]")