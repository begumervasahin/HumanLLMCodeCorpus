def count_matching_chars(source, example):
    count = 0
    for char in source:
        if char in example:
            count += 1
    return count
love_points = 0
vowels = "aeiuo"
consonants = "qrtpsdfghjklzxcvbnmy"
while True:
    try:
        name1, name2 = input("Input two names divided by comma (e.g. 'Jan, Joanna'): ").split(",")
        name1 = name1.lower().strip()
        name2 = name2.lower().strip()
        break
    except ValueError:
        print("Invalid input. Please provide two names separated by comma.")
if name1[0] == name2[0]:
    love_points += 20
if name1[0] in vowels and name2[0] in vowels:
    love_points += 10
if name1[0] in consonants and name2[0] in consonants:
    love_points += 5
if count_matching_chars(name1, vowels) == count_matching_chars(name2, vowels):
    love_points += 12
if count_matching_chars(name1, consonants) == count_matching_chars(name2, consonants):
    love_points += 12
if any(char in name1 and char in name2 for char in 'love'):
    love_points += 7
print(f"Your love points are {love_points}")
print("REMEMBER: Your relationship depends only on you and your partner, not on the stupid love calculator!")