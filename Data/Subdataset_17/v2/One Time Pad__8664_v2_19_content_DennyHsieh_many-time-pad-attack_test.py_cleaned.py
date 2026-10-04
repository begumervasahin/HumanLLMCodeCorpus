def main() -> None:
    char_a = 'A'
    char_space = ' '
    print(f"ord('A') = {hex(ord(char_a))}")
    print(f"ord(' ') = {hex(ord(char_space))}")
    xor_result = chr(ord(char_a) ^ ord(char_space))
    print(f"chr(ord('A') ^ ord(' ')) = {xor_result}")
if __name__ == "__main__":
    main()