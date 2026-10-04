
def combination_sum_aux(inputList, target):
    inputList.sort()
    resultList = []
    currentIndex = 0
    resultSeq = []
    combination_sum(inputList, target, currentIndex, resultSeq, resultList)
    return resultList
def combination_sum(inputList, target, currentIndex, resultSeq, resultList):
    for j in range(currentIndex, len(inputList)):
        num = inputList[j]
        if num > target:
            return
        resultSeq.append(num)
        if num < target:
            combination_sum(inputList, target - num, j, resultSeq, resultList)
        else:
            resultList.append(list(resultSeq))
        resultSeq.pop()
    return