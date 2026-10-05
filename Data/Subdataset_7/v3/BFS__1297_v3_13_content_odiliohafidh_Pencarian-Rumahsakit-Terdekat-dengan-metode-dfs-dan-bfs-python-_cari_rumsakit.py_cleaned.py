def fonk1(b9, start):
    b1 = [[start]]
    b2 = set()
    b3 = {'RS1', 'RS2', 'RS3'}
    while b1:
        b4 = b1.pop(0)
        b5 = b4[-1]
        if b5 in b3:
            return b4
        if b5 not in b2:
            for neighbor in b9.get(b5, []):
                b6 = b4 + [neighbor]
                b1.append(b6)
            b2.add(b5)
    return None
def fonk2(b9, start):
    b7 = [[start]]
    b2 = set()
    b3 = {'RS1', 'RS2', 'RS3'}
    while b7:
        b4 = b7.pop()
        b5 = b4[-1]
        if b5 in b3:
            return b4
        if b5 not in b2:
            for neighbor in b9.get(b5, []):
                b6 = b4 + [neighbor]
                b7.append(b6)
            b2.add(b5)
    return None
if b8 = = "__main__":
    b9 = {
        'A': {'RS1', 'C', 'E'},
        'B': {'E', 'D'},
        'C': {'A', 'B', 'RS2'},
        'D': {'B', 'F', 'K', 'RS3'},
        'E': {'A', 'B'},
        'F': {'D', 'G'},
        'G': {'H', 'F', 'I'},
        'H': {'G'},
        'I': {'G', 'J'},
        'J': {'I'},
        'K': {'D', 'L', 'M'},
        'L': {'RS2', 'K'},
        'M': {'K'},
        'RS1': {'A'},
        'RS2': {'C', 'L'},
        'RS3': {'D'}
    }
    b10 = input("Enter the starting b5: ")
    b11 = fonk1(b9, b10)
    b12 = fonk2(b9, b10)
    print("BFS Path:", b11)
    print("DFS Path:", b12)