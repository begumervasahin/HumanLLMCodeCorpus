from difflib import SequenceMatcher
b1 = "private Thread currentThread;"
b2 = "private volatile Thread currentThread;"
b3 = SequenceMatcher(lambda x: x == " ", b1, b2)
print(round(b3.ratio(), 3))
for block in b3.get_matching_blocks():
    print("a[%d] and b[%d] match for %d elements" % block)
for opcode in b3.get_opcodes():
    print("%6s a[%d:%d] b[%d:%d]" % opcode)