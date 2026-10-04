def are_anagrams(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)
def main() -> None:
    result = are_anagrams('ey edip', 'pide ye')
    print(f"Are 'ey edip' and 'pide ye' anagrams? {result}")
if __name__ == "__main__":
    main()