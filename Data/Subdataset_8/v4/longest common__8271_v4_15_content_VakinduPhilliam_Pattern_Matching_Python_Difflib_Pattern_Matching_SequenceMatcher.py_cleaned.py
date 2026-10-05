
from difflib import SequenceMatcher
string1 = "private Thread currentThread;"
string2 = "private volatile Thread currentThread;"
matcher = SequenceMatcher(lambda x: x == " ", string1, string2)
print(round(matcher.ratio(), 3))
for block in matcher.get_matching_blocks():
    print("In both strings, a[%d] and b[%d] match for %d elements" % block)
for opcode in matcher.get_opcodes():
    print("%6s for elements a[%d:%d] and b[%d:%d]" % opcode)