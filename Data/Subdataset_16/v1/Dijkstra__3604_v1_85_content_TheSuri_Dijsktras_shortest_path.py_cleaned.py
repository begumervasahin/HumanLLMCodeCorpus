import heapq
class class1:
    def fonk1(self):
        self.b1 = {}
    def fonk2(self, u, v, weight):
        if u not in self.b1:
            self.b1[u] = []
        if v not in self.b1:
            self.b1[v] = []
        self.b1[u].append((v, weight))
        self.b1[v].append((u, weight))
    def fonk3(self, b8):
        return self.b1.get(b8, [])
def fonk4(b9, a1, a2):
    b2 = []
    heapq.heappush(b2, (0, a1))
    b3 = set()
    b4 = {a1: None}
    b5 = {}
    while b2:
        curr_path_weight, b6 = heapq.heappop(b2)
        if b6 in b3:
            continue
        if b6 = = a2:
            return fonk5(a1, b6, b4), curr_path_weight
        for neighbor, edge_weight in b9.fonk3(b6):
            if neighbor not in b3 and (neighbor not in b5 or b5[neighbor] > curr_path_weight + edge_weight):
                b5[neighbor] = curr_path_weight + edge_weight
                b4[neighbor] = b6
                heapq.heappush(b2, (b5[neighbor], neighbor))
        b3.add(b6)
    return None, float('inf')
def fonk5(a1, a2, path_dict):
    b7 = []
    b8 = a2
    while b8 is not None:
        b7.append(b8)
        b8 = path_dict[b8]
    b7.reverse()
    return b7
def fonk6():
    b9 = class1()
    b9.fonk2(1, 2, 15)
    b9.fonk2(1, 3, 71)
    b9.fonk2(2, 3, 7)
    b9.fonk2(2, 4, 1)
    b9.fonk2(3, 4, 19)
    b9.fonk2(4, 3, 1)
    a1 = 1
    a2 = 4
    b4, b10 = fonk4(b9, a1, a2)
    if b4:
        print(f"Shortest b4 from {a1} to {a2}: {b4}")
        print(f"Total b10: {b10}")
    else:
        print(f"No b4 found from {a1} to {a2}")
if b11 = = "__main__":
    fonk6()