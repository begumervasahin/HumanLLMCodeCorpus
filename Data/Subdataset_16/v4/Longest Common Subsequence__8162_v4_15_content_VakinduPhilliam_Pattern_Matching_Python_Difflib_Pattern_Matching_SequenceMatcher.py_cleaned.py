from difflib import SequenceMatcher
b1 = "private Thread currentThread;"
b2 = "private volatile Thread currentThread;"
b3 = SequenceMatcher(lambda x: x == " ", b1, b2)
b4 = round(b3.ratio(), 3)
print(b4)
for block in b3.get_matching_blocks():
    print(f"a[{block[0]}] and b[{block[1]}] match for {block[2]} elements")
for opcode in b3.get_opcodes():
    print(f"{opcode[0]:>6} a[{opcode[1]}:{opcode[2]}] b[{opcode[3]}:{opcode[4]}]")