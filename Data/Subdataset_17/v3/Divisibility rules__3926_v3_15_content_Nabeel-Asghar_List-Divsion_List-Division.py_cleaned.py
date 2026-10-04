def division_func(listA, listB, c):
    result = [num for num in listA if sum(1 for divisor in listB if num % divisor == 0) >= c]
    print(set(result))
def main():
    inputA = input("Enter a list of numbers separated by spaces: ")
    listA = list(map(int, inputA.split()))
    inputB = input("Enter another list of numbers separated by spaces: ")
    listB = list(map(int, inputB.split()))
    c = len(listB)
    division_func(listA, listB, c)
if __name__ == "__main__":
    main()