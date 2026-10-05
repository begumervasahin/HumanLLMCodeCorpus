from difflib import SequenceMatcher
original_string = "private Thread currentThread;"
modified_string = "private volatile Thread currentThread;"
sequence_matcher = SequenceMatcher(lambda x: x == " ", original_string, modified_string)
similarity_ratio = round(sequence_matcher.ratio(), 3)
print("Similarity Ratio:", similarity_ratio)
print("Matching Blocks:")
for block in sequence_matcher.get_matching_blocks():
    a_start, b_start, length = block
    print(f"a[{a_start}] and b[{b_start}] match for {length} elements")
print("Operations to Transform:")
for operation in sequence_matcher.get_opcodes():
    operation_type, a_start, a_end, b_start, b_end = operation
    print(f"{operation_type:6} a[{a_start}:{a_end}] b[{b_start}:{b_end}]")