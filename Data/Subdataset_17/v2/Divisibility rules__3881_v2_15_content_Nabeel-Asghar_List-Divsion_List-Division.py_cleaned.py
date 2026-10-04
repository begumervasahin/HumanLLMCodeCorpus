def division_func(listA, listB, c):
    list_answer = []
    for num in listA:
        count = sum(1 for divisor in listB if num % divisor == 0)
        if count >= c:
            list_answer.append(num)
    list_answer = list(set(list_answer))
    print(list_answer)
def main():
    inputA = input("Enter a list of numbers separated by a space: ")
    listA = list(map(int, inputA.split()))
    inputB = input("Enter a list of numbers separated by a space: ")
    listB = list(map(int, inputB.split()))
    c = len(listB)
    division_func(listA, listB, c)
    input("Press any key to exit ")
if __name__ == "__main__":
    main()