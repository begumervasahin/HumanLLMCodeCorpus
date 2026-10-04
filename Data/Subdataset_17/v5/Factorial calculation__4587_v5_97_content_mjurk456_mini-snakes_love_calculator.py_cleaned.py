def count_characters(source, characters):
    return sum(1 for char in source if char in characters)
def calculate_love_points(name1, name2):
    vowels = "aeiou"
    consonants = "qrtpsdfghjklzxcvbnmy"
    special_letters = 'love'
    love_points = 0
    if name1[0] == name2[0]:
        love_points += 20
    if name1[0] in vowels and name2[0] in vowels:
        love_points += 10
    if name1[0] in consonants and name2[0] in consonants:
        love_points += 5
    if count_characters(name1, vowels) == count_characters(name2, vowels):
        love_points += 12
    if count_characters(name1, consonants) == count_characters(name2, consonants):
        love_points += 12
    if any(letter in name1 and letter in name2 for letter in special_letters):
        love_points += 7
    return love_points
def get_names_from_user():
    while True:
        try:
            input_string = input("Enter two names separated by a comma (e.g., 'Jan, Joanna'): ").strip()
            name1, name2 = [name.strip().lower() for name in input_string.split(",")]
            return name1, name2
        except ValueError:
            print("Invalid input. Please enter two names separated by a comma.")
def main():
    name1, name2 = get_names_from_user()
    love_points = calculate_love_points(name1, name2)
    print(f"Your love points are {love_points}.")
    print("REMEMBER: your relationship depends on you and your partner, not on this silly love calculator!")
if __name__ == "__main__":
    main()