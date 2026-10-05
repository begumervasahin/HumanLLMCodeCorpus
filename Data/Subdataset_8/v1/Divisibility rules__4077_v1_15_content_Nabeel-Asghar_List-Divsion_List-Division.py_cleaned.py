def divisionFunc(listA, listB, c):
    listAnswer = []
    for i in listA:
        count = 0
        for j in listB:
            if i % j == 0:
                count += 1
        if count >= c:
            listAnswer.append(i)
    listAnswer = set(listAnswer)
    print(listAnswer)
def main():
    inputA = input("Enter a list of numbers separated by a space: ")
    listA = list(map(int, inputA.split(' ')))
    inputB = input("Enter a list of numbers separated by a space: ")
    listB = list(map(int, inputB.split(' ')))
    c = len(listB) / 2
    divisionFunc(listA, listB, c)
    k = input("Press any key to exit ")
if __name__ == "__main__":
    main()