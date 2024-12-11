
b1 = {
    'ALASKA': {'CALIFORNIA'},
    'CALIFORNIA': {'CAROLINA', 'ALASKA'},
    'CAROLINA': {'CALIFORNIA', 'INDIANA', 'HAWAII', 'DAREWALE'},
    'DAREWALE': {'CAROLINA', 'EDINBURGH', 'HAWAII', 'FLORIDA'},
    'EDINBURGH': {'DAREWALE'},
    'FLORIDA': {'DAREWALE', 'GEORGIA'},
    'GEORGIA': {'FLORIDA', 'HAWAII'},
    'HAWAII': {'DARAWALE', 'CAROLINA', 'GEORGIA', 'LOUSIANA'},
    'INDIANA': {'CAROLINA', 'IDAKO', 'KENTUCKY'},
    'IDAKO': {'INDIANA'},
    'KENTUCKY': {'LOUSIANA', 'INDIANA'},
    'LOUSIANA': {'KENTUCKY', 'HAWAII'}
}
def fonk1(graph, start, finish):
    b2 = [[start]]
    b3 = set()
    while b2:
        b4 = b2.pop()
        b5 = b4[-1]
        if b5 = = finish:
            return b4
        elif b5 not in b3:
            for branch in graph.get(b5, []):
                b6 = list(b4)
                b6.append(branch)
                b2.append(b6)
            b3.add(b5)
    print("NOT FOUND 404")
print(fonk1(b1, 'ALASKA', 'INDIANA'))