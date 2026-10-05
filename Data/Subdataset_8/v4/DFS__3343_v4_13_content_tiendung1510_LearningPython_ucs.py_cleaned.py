import queue
from mymap import myMap
from modules import showResultWithAttr, showStep, aweSomeSort
def UCS(start, goal):
    q = queue.deque()
    q.append(start)
    previous = {city: {'from': None, 'total_cost': 0} for city in myMap.keys()}
    counter = 0
    while True:
        counter += 1
        showStep(counter, q, previous)
        curCity = q.popleft()
        curCityTotalCost = previous[curCity]['total_cost']
        if curCity != goal:
            for city, attrs in myMap[curCity].items():
                cityTotalCost = previous[city]['total_cost']
                totalCost = attrs['cost'] + curCityTotalCost
                if previous[city]['from'] is None or totalCost < cityTotalCost:
                    if city in q:
                        q.remove(city)
                    q.append(city)
                    previous[city]['from'] = curCity
                    previous[city]['total_cost'] = totalCost
        else:
            showResultWithAttr(previous, start, goal)
            return True
        if len(q) == 0:
            break
        q = queue.deque(aweSomeSort(q, previous))
    return False