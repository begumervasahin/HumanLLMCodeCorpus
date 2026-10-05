def counting(source, example):
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
        print("Wrong input")
if name1[0] == name2[0]:
    love_points += 20
if (name1[0] in vowels) and (name2[0] in vowels):
    love_points += 10
if (name1[0] in consonants) and (name2[0] in consonants):
    love_points += 5
if counting(name1, vowels) == counting(name2, vowels):
    love_points += 12
if counting(name1, consonants) == counting(name2, consonants):
    love_points += 12
if ('l' in name1 and 'l' in name2) or ('o' in name1 and 'o' in name2) \
        or ('v' in name1 and 'v' in name2) or ('e' in name1 and 'e' in name2):
    love_points += 7
print("Your love points are %d" % love_points)
print("REMEMBER: your relationship depends only on you and your partner, not from the stupid love calculator!")