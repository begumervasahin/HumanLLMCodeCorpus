def fonk1(graph, start, finish):
    b1 = [[start]]
    b2 = set()
    while b1:
        b3 = b1.pop()
        b4 = b3[-1]
        if b4 = = finish:
            return b3
        if b4 not in b2:
            for branch in graph.get(b4, []):
                b5 = b3 + [branch]
                b1.append(b5)
            b2.add(b4)
    print("NOT FOUND 404")
    return None
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
print(fonk1(b6, 'ALASKA', 'INDIANA'))