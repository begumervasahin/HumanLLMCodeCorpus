from exceptions import NotImplementedError
import heapq
def fonk1(graph, source, target):
  b1 = []
  heapq.heappush(b1, (0, source))
  b2 = set()
  b3 = {source: None}
  b4 = dict()
  while(b1):
    b5 = heapq.heappop(b1)
    b6 = b5[0]
    b7 = b5[1]
    if b7 in b2:
      continue
    elif b7 = = target:
      print(fonk2(source, b7, b3))
      return (fonk2(source, b7, b3), b6)
    for neighbor, edge_weight in graph.get_neighbors(b7):
      if neighbor not in b2 and (neighbor not in b4 or b4[neighbor] > b6+edge_weight):
        b4[neighbor] = b6 + edge_weight
        b3[neighbor] = b7
        heapq.heappush(b1, (b4[neighbor], neighbor))
    b2.add(b7)
  return None
def fonk2(source, target, path_dict):
  b8 = list()
  b9 = target
  while b9 != None:
    b8.append(b9)
    b9 = path_dict[b9]
  return b8