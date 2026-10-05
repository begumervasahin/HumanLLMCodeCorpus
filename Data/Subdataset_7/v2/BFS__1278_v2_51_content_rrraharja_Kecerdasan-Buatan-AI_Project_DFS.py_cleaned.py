def fonk1(graph, start, goal):
    b1 = [[start]]
    b2 = set()
    while b1:
        b3 = b1.pop()
        b4 = b3[-1]
        if b4 = = goal:
            return b3
        elif b4 not in b2:
            for neighbor in graph.get(b4, []):
                b5 = list(b3)
                b5.append(neighbor)
                b1.append(b5)
            b2.add(b4)
    print("Goal b4 not found.")
b6 = {
    'ALASKA': {'CALIFORNIA'},
    'CALIFORNIA': {'CAROLINA', 'ALASKA'},
    'CAROLINA': {'CALIFORNIA', 'INDIANA', 'HAWAII', 'DAREWALE'},
    'DAREWALE': {'CAROLINA', 'EDINBURGH', 'HAWAII', 'FLORIDA'},
    'EDINBURGH': {'DAREWALE'},
    'FLORIDA': {'DAREWALE', 'GEORGIA'},
    'GEORGIA': {'FLORIDA', 'HAWAII'},
    'HAWAII': {'DAREWALE', 'CAROLINA', 'GEORGIA', 'LOUSIANA'},
    'INDIANA': {'CAROLINA', 'IDAKO', 'KENTUCKY'},
    'IDAKO': {'INDIANA'},
    'KENTUCKY': {'LOUSIANA', 'INDIANA'},
    'LOUSIANA': {'KENTUCKY', 'HAWAII'}
}
b7 = 'ALASKA'
b8 = 'INDIANA'
b9 = fonk1(b6, b7, b8)
print(b9)