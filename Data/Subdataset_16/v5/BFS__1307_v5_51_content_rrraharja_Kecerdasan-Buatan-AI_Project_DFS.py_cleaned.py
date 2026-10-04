
b1 = {
    'ALASKA': {'CALIFORNIA'},
    'CALIFORNIA': {'CAROLINA', 'ALASKA'},
    'CAROLINA': {'CALIFORNIA', 'INDIANA', 'HAWAII', 'DAREWALE'},
    'DAREWALE': {'CAROLINA', 'EDINBURGH', 'HAWAII', 'FLORIDA'},
    'EDINBURGH': {'DAREWALE'},
    'FLORIDA': {'DAREWALE', 'GEORGIA'},
    'GEORGIA': {'FLORIDA', 'HAWAII'},
    'HAWAII': {'DAREWALE', 'CAROLINA', 'GEORGIA', 'LOUISIANA'},
    'INDIANA': {'CAROLINA', 'IDAHO', 'KENTUCKY'},
    'IDAHO': {'INDIANA'},
    'KENTUCKY': {'LOUISIANA', 'INDIANA'},
    'LOUISIANA': {'KENTUCKY', 'HAWAII'}
}
def fonk1(graph, start, goal):
    b2 = [[start]]
    b3 = set()
    while b2:
        b4 = b2.pop()
        b5 = b4[-1]
        if b5 = = goal:
            return b4
        if b5 not in b3:
            b3.add(b5)
            for neighbor in graph.get(b5, []):
                b6 = b4 + [neighbor]
                b2.append(b6)
    return None
if b7 = = "__main__":
    b8 = 'ALASKA'
    b9 = 'INDIANA'
    b4 = fonk1(b1, b8, b9)
    if b4:
        print(f"Path found: {' -> '.join(b4)}")
    else:
        print("No b4 found")