def quicksort_Spivot(qPArr, start, end):
    size = end - start + 1
    stack = [0] * size
    top = -1
    top = top + 1
    stack[top] = start
    top = top + 1
    stack[top] = end
    while top >= 0:
        end = stack[top]
        top = top - 1
        start = stack[top]
        top = top - 1
        i = start - 1
        pv = qPArr[end]
        for j in range(start, end):
            if qPArr[j] <= pv:
                i = i + 1
                qPArr[i], qPArr[j] = qPArr[j], qPArr[i]
        qPArr[i + 1], qPArr[end] = qPArr[end], qPArr[i + 1]
        pv = i + 1
        if abs(start - pv) < abs(pv - end):
            if pv + 1 < end:
                top = top + 1
                stack[top] = pv + 1
                top = top + 1
                stack[top] = end
            if pv - 1 > start:
                top = top + 1
                stack[top] = start
                top = top + 1
                stack[top] = pv - 1
        else:
            if pv - 1 > start:
                top = top + 1
                stack[top] = start
                top = top + 1
                stack[top] = pv - 1
            if pv + 1 < end:
                top = top + 1
                stack[top] = pv + 1
                top = top + 1
                stack[top] = end
def gq(arrGQ):
    quicksort_Spivot(arrGQ, 0, len(arrGQ) - 1)
    print("---GQ---")
    for x in range(len(arrGQ) - 1, -1, -1):
        if len(arrGQ) - x == arrGQ[x]:
            print(arrGQ[x])
            break
        elif len(arrGQ) - x >= arrGQ[x]:
            print(len(arrGQ) - x - 1)
            break
        elif x == 0:
            print(len(arrGQ))
def main():
    print("Enter value Of n:")
    n = int(input().strip())
    print("Enter array in format [1, 2, 3]:")
    arr = list(map(int, input().strip()[1:-1].strip().split(',')))
    if len(arr) == n:
        gq(arr)
    else:
        print("Error: N and array size don't match. Exiting Program.")
if __name__ == "__main__":
    main()