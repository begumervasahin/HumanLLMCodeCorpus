import queue
from mymap import myMap
from modules import showResultWithAttr, showStep, aweSomeSort
def UCS(start, goal):
    priority_queue = queue.PriorityQueue()
    priority_queue.put((0, start))
    previous = {city: {'from': None, 'total_cost': float('inf')} for city in myMap.keys()}
    previous[start] = {'from': None, 'total_cost': 0}
    counter = 0
    while not priority_queue.empty():
        counter += 1
        showStep(counter, priority_queue.queue, previous)
        cur_cost, curCity = priority_queue.get()
        if curCity != goal:
            for nextCity, attrs in myMap[curCity].items():
                totalCost = cur_cost + attrs['cost']
                if totalCost < previous[nextCity]['total_cost']:
                    previous[nextCity]['from'] = curCity
                    previous[nextCity]['total_cost'] = totalCost
                    priority_queue.put((totalCost, nextCity))
        else:
            showResultWithAttr(previous, start, goal)
            return True
    return False
start_city = 'A'
goal_city = 'B'
UCS(start_city, goal_city)