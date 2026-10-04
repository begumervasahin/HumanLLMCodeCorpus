from difflib import SequenceMatcher
string_a = "private Thread currentThread;"
string_b = "private volatile Thread currentThread;"
matcher = SequenceMatcher(lambda x: x == " ", string_a, string_b)
similarity_ratio = round(matcher.ratio(), 3)
print(f"Similarity ratio: {similarity_ratio}")
print("Matching blocks:")
for block in matcher.get_matching_blocks():
    print(f"a[{block[0]}] and b[{block[1]}] match for {block[2]} elements")
print("Opcodes:")
for opcode in matcher.get_opcodes():
    print(f"{opcode[0].capitalize():>7} a[{opcode[1]}:{opcode[2]}] b[{opcode[3]}:{opcode[4]}]")