import queue
from mymap import myMap
from modules import showResultWithAttr, showStep, aweSomeSort
def fonk1(start, goal):
    b1 = queue.PriorityQueue()
    b1.put((0, start))
    b2 = {city: {'from': None, 'total_cost': float('inf')} for city in myMap.keys()}
    b2[start] = {'from': None, 'total_cost': 0}
    a1 = 0
    while not b1.empty():
        a1 += 1
        showStep(a1, b1.queue, b2)
        cur_cost, b3 = b1.get()
        if b3 != goal:
            for nextCity, attrs in myMap[b3].items():
                b4 = cur_cost + attrs['cost']
                if b4 < b2[nextCity]['total_cost']:
                    b2[nextCity]['from'] = b3
                    b2[nextCity]['total_cost'] = b4
                    b1.put((b4, nextCity))
        else:
            showResultWithAttr(b2, start, goal)
            return True
    return False
b5 = 'A'
b6 = 'B'
fonk1(b5, b6)