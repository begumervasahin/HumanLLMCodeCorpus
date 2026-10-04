def division_func(listA, listB, c):
    list_answer = []
    for i in listA:
        count = 0
        for j in listB:
            if i % j == 0:
                count += 1
        if count >= c:
            list_answer.append(i)
    list_answer = set(list_answer)
    print(list_answer)
inputA = input("Enter a list of numbers separated by a space: ")
listA = list(map(int, inputA.split()))
inputB = input("Enter a list of numbers separated by a space: ")
listB = list(map(int, inputB.split()))
c = len(listB)
division_func(listA, listB, c)
input("Press any key to exit ")