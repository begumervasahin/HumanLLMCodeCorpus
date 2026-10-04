b1 = SequenceMatcher(lambda x: x == " ",
                        "private Thread currentThread;",
                        "private volatile Thread currentThread;")
print(round(b1.ratio(), 3))
for block in b1.get_matching_blocks():
           print("a[%d] and b[%d] match for %d elements" % block)
for opcode in b1.get_opcodes():
           print("%6s a[%d:%d] b[%d:%d]" % opcode)