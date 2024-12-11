import queue
from mymap import myMap
from modules import showResultWithAttr, showStep, aweSomeSort
def fonk1(start, goal):
  b1 = queue.deque()
  b1.append(start)
  b2 = []
  for city in myMap.keys():
    b2.append((city, {'from': None, 'total_cost': 0}))
  b2 = dict(b2)
  a1 = 0
  while 1:
    a1 += 1
    showStep(a1, b1, b2)
    b3 = b1.popleft()
    b4 = b2[b3]['total_cost']
    if b3 != goal:
      for city in myMap[b3].keys():
        b5 = b2[city]['total_cost']
        b6 = myMap[b3][city]['cost'] + b4
        if b2[city]['from'] == None or b6 < b5 :
          if b1.count(city) != 0:
            b1.remove(city)
          b1.append(city)
          b2[city]['from'] =  b3
          b2[city]['total_cost'] = b6
    else:
      showResultWithAttr(b2, start, goal)
      return True
    if len(b1) == 0: break
    b1 = queue.deque(aweSomeSort(b1, b2))
  return False