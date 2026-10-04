def are_anagrams(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    s2_list = list(s2)
    for char in s1:
        if char in s2_list:
            s2_list.remove(char)
        else:
            return False
    return True
def main() -> None:
    print(are_anagrams('ey edip', 'pide ye'))
if __name__ == "__main__":
    main()