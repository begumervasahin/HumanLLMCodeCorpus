import random
def linear_search(data, target):
    for number in data:
        if number == target:
            return True
    return False
def main():
    data = [1, 2, 3, 4, 5, 6]
    target = random.randrange(1, 10)
    print("List of numbers:", data)
    print("Target value to search:", target)
    result = linear_search(data, target)
    print("Target value found:", result)
if __name__ == "__main__":
    main()