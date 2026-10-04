def division_func(listA, listB, c):
    list_answer = [i for i in listA if sum(1 for j in listB if i % j == 0) >= c]
    list_answer = set(list_answer)
    print(list_answer)
def main():
    inputA = input("Enter a list of numbers separated by a space: ")
    listA = list(map(int, inputA.split()))
    inputB = input("Enter another list of numbers separated by a space: ")
    listB = list(map(int, inputB.split()))
    c = len(listB)
    division_func(listA, listB, c)
if __name__ == "__main__":
    main()