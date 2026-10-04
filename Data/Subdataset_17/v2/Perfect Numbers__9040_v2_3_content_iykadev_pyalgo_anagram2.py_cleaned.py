def are_anagrams(s1: str, s2: str) -> bool:
    cleaned_s1 = s1.replace(" ", "").lower()
    cleaned_s2 = s2.replace(" ", "").lower()
    sorted_s1 = sorted(cleaned_s1)
    sorted_s2 = sorted(cleaned_s2)
    return sorted_s1 == sorted_s2
if __name__ == "__main__":
    test_result = are_anagrams('ey edip', 'pide ye')
    print(test_result)
