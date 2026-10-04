def are_anagrams(s1: str, s2: str) -> bool:
    cleaned_s1 = s1.replace(" ", "").lower()
    cleaned_s2 = s2.replace(" ", "").lower()
    return sorted(cleaned_s1) == sorted(cleaned_s2)
def main() -> None:
    s1 = 'ey edip'
    s2 = 'pide ye'
    result = are_anagrams(s1, s2)
    print(f"Are '{s1}' and '{s2}' anagrams? {result}")
if __name__ == "__main__":
    main()