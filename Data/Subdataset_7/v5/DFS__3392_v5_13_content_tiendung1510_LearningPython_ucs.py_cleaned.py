import queue
from mymap import myMap
from modules import showResultWithAttr, showStep, aweSomeSort
def fonk1(start, goal):
    b1 = queue.deque()
    b1.append(start)
    b2 = {city: {'from': None, 'b6': 0} for city in myMap.keys()}
    a1 = 0
    while True:
        a1 += 1
        showStep(a1, b1, b2)
        b3 = b1.popleft()
        b4 = b2[b3]['b6']
        if b3 = = goal:
            showResultWithAttr(b2, start, goal)
            return True
        for next_city, attrs in myMap[b3].items():
            b5 = b2[next_city]['b6']
            b6 = attrs['cost'] + b4
            if b2[next_city]['from'] is None or b6 < b5:
                if next_city in b1:
                    b1.remove(next_city)
                b1.append(next_city)
                b2[next_city]['from'] = b3
                b2[next_city]['b6'] = b6
        if len(b1) == 0:
            break
        b1 = queue.deque(aweSomeSort(b1, b2))
    return False