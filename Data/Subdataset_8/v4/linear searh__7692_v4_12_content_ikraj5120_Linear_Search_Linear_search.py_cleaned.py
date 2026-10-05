import time
from matplotlib import pyplot as plt
test_case = [y for y in range(1000)]
result = []
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
def test(L):
    for j in range(0, len(L)):
        start_time = time.time()
        flag = search(L, j)
        end_time = time.time()
        if flag:
            result.append(end_time - start_time)
    return result
def show_results(L, res):
    plt.plot(L, res, color='green', marker='o', linestyle='solid')
    plt.title("Linear Search Performance")
    plt.xlabel('List Elements')
    plt.ylabel('Execution Time (s)')
    plt.show()
test(test_case)
show_results(test_case, result)