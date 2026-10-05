b1 = {
    'ALASKA': set(['CALIFORNIA']),
    'CALIFORNIA': set(['CAROLINA', 'ALASKA']),
    'CAROLINA': set(['CALIFORNIA', 'INDIANA', 'HAWAII', 'DAREWALE']),
    'DAREWALE': set(['CAROLINA', 'EDINBURGH', 'HAWAII', 'FLORIDA']),
    'EDINBURGH': set(['DAREWALE']),
    'FLORIDA': set(['DAREWALE', 'GEORGIA']),
    'GEORGIA': set(['FLORIDA', 'HAWAII']),
    'HAWAII': set(['DAREWALE', 'CAROLINA', 'GEORGIA', 'LOUSIANA']),
    'INDIANA': set(['CAROLINA', 'IDAKO', 'KENTUCKY']),
    'IDAKO': set(['INDIANA']),
    'KENTUCKY': set(['LOUSIANA', 'INDIANA']),
    'LOUSIANA': set(['KENTUCKY', 'HAWAII'])
}
def fonk1(graf, start, finish):
    b2 = [[start]]
    b3 = set()
    while b2:
        b4 = b2.pop()
        b5 = b4[-1]
        if b5 = = finish:
            return b4
        elif b5 not in b3:
            for branch in graf.get(b5, []):
                b6 = list(b4)
                b6.append(branch)
                b2.append(b6)
            b3.add(b5)
    print("NOT FOUND 404")
b7 = 'ALASKA'
b8 = 'INDIANA'
b9 = fonk1(b1, b7, b8)
print(b9)