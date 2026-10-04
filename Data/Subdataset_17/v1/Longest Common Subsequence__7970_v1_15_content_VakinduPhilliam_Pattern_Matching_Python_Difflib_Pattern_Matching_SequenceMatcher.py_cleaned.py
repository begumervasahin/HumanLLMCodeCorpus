from difflib import SequenceMatcher
a = "private Thread currentThread;"
b = "private volatile Thread currentThread;"
s = SequenceMatcher(lambda x: x == " ", a, b)
print(round(s.ratio(), 3))
for block in s.get_matching_blocks():
    print("a[%d] and b[%d] match for %d elements" % block)
for opcode in s.get_opcodes():
    print("%6s a[%d:%d] b[%d:%d]" % opcode)