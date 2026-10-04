def division_func(listA, listB, c):
    result = {i for i in listA if sum(1 for j in listB if i % j == 0) >= c}
    print(result)
def main():
    try:
        inputA = input("Enter a list of numbers separated by spaces: ")
        listA = list(map(int, inputA.split()))
        inputB = input("Enter another list of numbers separated by spaces: ")
        listB = list(map(int, inputB.split()))
        c = len(listB)
        division_func(listA, listB, c)
    except ValueError:
        print("Please enter valid lists of integers.")
if __name__ == "__main__":
    main()