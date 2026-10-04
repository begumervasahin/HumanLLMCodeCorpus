from difflib import SequenceMatcher
def main():
    string_a = "private Thread currentThread;"
    string_b = "private volatile Thread currentThread;"
    matcher = SequenceMatcher(lambda x: x == " ", string_a, string_b)
    similarity_ratio = round(matcher.ratio(), 3)
    print(f"Similarity ratio: {similarity_ratio}")
    print("\nMatching blocks:")
    for block in matcher.get_matching_blocks():
        a_index, b_index, size = block
        print(f"a[{a_index}] and b[{b_index}] match for {size} elements")
    print("\nOpcodes:")
    for opcode in matcher.get_opcodes():
        tag, i1, i2, j1, j2 = opcode
        print(f"{tag.capitalize():>7} a[{i1}:{i2}] b[{j1}:{j2}]")
if __name__ == "__main__":
    main()