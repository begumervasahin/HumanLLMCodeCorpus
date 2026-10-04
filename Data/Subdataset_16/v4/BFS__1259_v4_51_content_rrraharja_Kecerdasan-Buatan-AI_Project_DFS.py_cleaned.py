
b1 = {
    'ALASKA': set(['CALIFORNIA']),
    'CALIFORNIA': set(['CAROLINA', 'ALASKA']),
    'CAROLINA': set(['CALIFORNIA', 'INDIANA', 'HAWAII', 'DAREWALE']),
    'DAREWALE': set(['CAROLINA', 'EDINBURGH', 'HAWAII', 'FLORIDA']),
    'EDINBURGH': set(['DAREWALE']),
    'FLORIDA': set(['DAREWALE', 'GEORGIA']),
    'GEORGIA': set(['FLORIDA', 'HAWAII']),
    'HAWAII': set(['DAREWALE', 'CAROLINA', 'GEORGIA', 'LOUISIANA']),
    'INDIANA': set(['CAROLINA', 'IDAHO', 'KENTUCKY']),
    'IDAHO': set(['INDIANA']),
    'KENTUCKY': set(['LOUISIANA', 'INDIANA']),
    'LOUISIANA': set(['KENTUCKY', 'HAWAII'])
}
def fonk1(graph, start, goal):
    b2 = [[start]]
    b3 = set()
    while b2:
        b4 = b2.pop()
        b5 = b4[-1]
        if b5 = = goal:
            return b4
        elif b5 not in b3:
            for neighbor in graph.get(b5, []):
                b6 = list(b4)
                b6.append(neighbor)
                b2.append(b6)
            b3.add(b5)
    print("Path not found")
    return None
if b7 = = "__main__":
    b4 = fonk1(b1, 'ALASKA', 'INDIANA')
    if b4:
        print(f"Path found: {' -> '.join(b4)}")
    else:
        print("No b4 found")