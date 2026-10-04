def is_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)
def main():
    str1 = 'ey edip'
    str2 = 'pide ye'
    result = is_anagram(str1, str2)
    print(f"'{str1}' and '{str2}' are anagrams: {result}")
if __name__ == "__main__":
    main()