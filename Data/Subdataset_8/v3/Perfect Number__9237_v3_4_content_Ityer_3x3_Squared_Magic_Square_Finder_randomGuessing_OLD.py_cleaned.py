import random
import pickle
results = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: []
}
limit = 15
loops = 100
dupes = 0
def display_results():
    print("One (may contain duplicates):")
    print(len(results[1]))
    for i in range(2, 8):
        print(f"{i}:")
        print(len(results[i]))
        print(results[i])
    print("Win:")
    print(len(results[8]))
    print(results[8])
    print(f"{dupes} Duplicates Removed")
def save_results():
    with open("Win.txt", 'wb') as f:
        pickle.dump(results[8], f)
    for i in range(2, 8):
        filename = f"{i}.txt"
        with open(filename, 'wb') as f:
            pickle.dump(results[i], f)
    with open("Fail.txt", 'wb') as f:
        pickle.dump(results[1], f)
def categorize_results(answers, numbers):
    occurrences = answers.count(max(answers, key=answers.count))
    results[occurrences].append(numbers)
    print(sum(len(results[i]) for i in range(1, 9)))
def main():
    global dupes
    for _ in range(loops):
        tmp = False
        numbers = []
        for _ in range(9):
            while not tmp:
                num = random.randint((limit * -1), limit)
                if (num not in numbers) and (num < limit):
                    numbers.append(num)
                    tmp = True
            tmp = False
        if numbers not in results.values():
            squares = [num ** 2 for num in numbers]
            horizontal_sums = [sum(squares[i:i+3]) for i in range(0, len(squares), 3)]
            vertical_sums = [sum(squares[i::3]) for i in range(3)]
            diagonal_sums = [sum(squares[::4]), sum(squares[2:7:2])]
            answers = horizontal_sums + vertical_sums + diagonal_sums
            categorize_results(answers, numbers)
        else:
            print("Duplicate Found")
            dupes += 1
if __name__ == "__main__":
    main()
    display_results()
    save_results()