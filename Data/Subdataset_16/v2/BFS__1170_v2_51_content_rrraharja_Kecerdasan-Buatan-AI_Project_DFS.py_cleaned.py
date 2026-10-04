
b1 = {
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
    return "NOT FOUND 404"
if b7 = = "__main__":
    b8 = 'ALASKA'
    b9 = 'INDIANA'
    b4 = fonk1(b1, b8, b9)
    print(f"Path from {b8} to {b9}: {b4}")