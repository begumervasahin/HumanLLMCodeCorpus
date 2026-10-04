def counting(source, example):
    count = 0
    for char in source:
        if char in example:
            count += 1
    return count
def main():
    love_points = 0
    vowels = "aeiou"
    consonants = "qrtpsdfghjklzxcvbnmy"
    while True:
        try:
            names = input("Input two names separated by a comma (e.g., 'Jan, Joanna'): ").split(",")
            name1, name2 = names[0].strip().lower(), names[1].strip().lower()
            break
        except (IndexError, ValueError):
            print("Invalid input. Please enter two names separated by a comma.")
    if name1[0] == name2[0]:
        love_points += 20
    if name1[0] in vowels and name2[0] in vowels:
        love_points += 10
    if name1[0] in consonants and name2[0] in consonants:
        love_points += 5
    if counting(name1, vowels) == counting(name2, vowels):
        love_points += 12
    if counting(name1, consonants) == counting(name2, consonants):
        love_points += 12
    if any(letter in name1 and letter in name2 for letter in 'love'):
        love_points += 7
    print(f"Your love points are {love_points}")
    print("REMEMBER: your relationship depends only on you and your partner, not on this silly love calculator!")
if __name__ == "__main__":
    main()