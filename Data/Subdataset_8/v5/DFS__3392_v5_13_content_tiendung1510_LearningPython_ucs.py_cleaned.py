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
        cur_city = q.popleft()
        cur_city_total_cost = previous[cur_city]['total_cost']
        if cur_city == goal:
            showResultWithAttr(previous, start, goal)
            return True
        for next_city, attrs in myMap[cur_city].items():
            next_city_total_cost = previous[next_city]['total_cost']
            total_cost = attrs['cost'] + cur_city_total_cost
            if previous[next_city]['from'] is None or total_cost < next_city_total_cost:
                if next_city in q:
                    q.remove(next_city)
                q.append(next_city)
                previous[next_city]['from'] = cur_city
                previous[next_city]['total_cost'] = total_cost
        if len(q) == 0:
            break
        q = queue.deque(aweSomeSort(q, previous))
    return False