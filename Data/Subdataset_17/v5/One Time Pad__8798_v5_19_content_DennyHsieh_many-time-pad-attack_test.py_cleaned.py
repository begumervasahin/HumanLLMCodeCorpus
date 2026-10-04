def demonstrate_ord_chr_xor():
    char_a = 'A'
    char_space = ' '
    ord_a = ord(char_a)
    ord_space = ord(char_space)
    print(f"ord('A') = {hex(ord_a)}")
    print(f"ord(' ') = {hex(ord_space)}")
    axorb = chr(ord_a ^ ord_space)
    print(f"chr(ord('A') ^ ord(' ')) = {axorb}")
def main():
    demonstrate_ord_chr_xor()
if __name__ == "__main__":
    main()