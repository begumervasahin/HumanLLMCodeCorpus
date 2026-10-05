import queue
from mymap import myMap
from modules import showResultWithAttr, showStep, aweSomeSort
def UCS(start, goal):
    q = queue.PriorityQueue()
    q.put((0, start))
    previous = {city: {'from': None, 'total_cost': float('inf')} for city in myMap.keys()}
    previous[start] = {'from': None, 'total_cost': 0}
    counter = 0
    while not q.empty():
        counter += 1
        showStep(counter, q.queue, previous)
        cur_cost, curCity = q.get()
        if curCity != goal:
            for nextCity, attrs in myMap[curCity].items():
                totalCost = cur_cost + attrs['cost']
                if totalCost < previous[nextCity]['total_cost']:
                    previous[nextCity]['from'] = curCity
                    previous[nextCity]['total_cost'] = totalCost
                    q.put((totalCost, nextCity))
        else:
            showResultWithAttr(previous, start, goal)
            return True
    return False
start_city = 'A'
goal_city = 'B'
UCS(start_city, goal_city)