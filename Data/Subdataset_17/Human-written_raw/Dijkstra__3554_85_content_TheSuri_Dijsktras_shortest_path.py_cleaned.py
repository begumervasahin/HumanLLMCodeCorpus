from exceptions import NotImplementedError
import heapq
def shortest_path(graph, source, target):
  priority_q = []
  heapq.heappush(priority_q, (0, source))
  visited = set()
  path = {source: None}
  remaining = dict()
  while(priority_q):
    visting_node = heapq.heappop(priority_q)
    curr_path_weight = visting_node[0]
    curr_node = visting_node[1]
    if curr_node in visited:
      continue
    elif curr_node == target:
      print(get_path(source, curr_node, path))
      return (get_path(source, curr_node, path), curr_path_weight)
    for neighbor, edge_weight in graph.get_neighbors(curr_node):
      if neighbor not in visited and (neighbor not in remaining or remaining[neighbor] > curr_path_weight+edge_weight):
        remaining[neighbor] = curr_path_weight + edge_weight
        path[neighbor] = curr_node
        heapq.heappush(priority_q, (remaining[neighbor], neighbor))
    visited.add(curr_node)
  return None
def get_path(source, target, path_dict):
  result = list()
  node = target
  while node != None:
    result.append(node)
    node = path_dict[node]
  return result