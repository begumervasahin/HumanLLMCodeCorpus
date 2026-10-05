from difflib import SequenceMatcher
string1 = "private Thread currentThread;"
string2 = "private volatile Thread currentThread;"
s = SequenceMatcher(lambda x: x == " ", string1, string2)
print(round(s.ratio(), 3))
for block in s.get_matching_blocks():
    print("a[%d] and b[%d] match for %d elements" % block)
for opcode in s.get_opcodes():
    print("%6s a[%d:%d] b[%d:%d]" % opcode)