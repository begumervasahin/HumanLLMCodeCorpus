def is_anagram(s1, s2):
    def clean_string(s):
        return s.replace(" ", "").lower()
    cleaned_s1 = clean_string(s1)
    cleaned_s2 = clean_string(s2)
    return sorted(cleaned_s1) == sorted(cleaned_s2)
def main():
    s1 = 'ey edip'
    s2 = 'pide ye'
    result = is_anagram(s1, s2)
    print(f"'{s1}' and '{s2}' are anagrams: {result}")
if __name__ == "__main__":
    main()