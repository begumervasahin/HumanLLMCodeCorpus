import random
def rand(dig):
    nums = []
    for x in range(dig):
        nums.append(str(random.randint(0, 9)))
    num = "".join(nums)
    return num
def main():
    length = 10
    random_number = rand(length)
    print(f"Random number of length {length}: {random_number}")
if __name__ == "__main__":
    main()