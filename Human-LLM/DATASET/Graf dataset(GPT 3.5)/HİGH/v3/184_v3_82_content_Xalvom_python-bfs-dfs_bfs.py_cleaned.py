from collections import deque
def fonk1(b6, b7, b8):
    b1 = deque([[b7]])
    b2 = set()
    while b1:
        b3 = b1.popleft()
        b4 = b3[-1]
        if b4 = = b8:
            return b3
        elif b4 not in b2:
            for neighbor in b6.get(b4, []):
                b5 = b3 + [neighbor]
                b1.append(b5)
            b2.add(b4)
    print("Tidak ditemukan")
    return None
b6 = {
    'A': {'B'},
    'B': {'A', 'C'},
    'C': {'B', 'D', 'H', 'I'},
    'D': {'C', 'E', 'F', 'H', 'M'},
    'E': {'D'},
    'F': {'D', 'G', 'M'},
    'G': {'F', 'H'},
    'H': {'C', 'D', 'G', 'L'},
    'I': {'C', 'J', 'K'},
    'J': {'I'},
    'K': {'I', 'L'},
    'L': {'H', 'K'},
    'M': {'D', 'F'}
}
print("********* BFS ***********")
b7 = input("Input Awal: ")
b8 = input("Input Tujuan: ")
print("**************************")
print()
b9 = fonk1(b6, b7, b8)
if b9:
    print("Jalur BFS:", b9)
else:
    print("Tidak ditemukan")
print()
print("Link Github: https: