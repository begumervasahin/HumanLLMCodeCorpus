aunsorted = [6, 2, 7, 8, 3, 1, 10, 5, 4, 9]
asorted = []
while aunsorted:
    amin = aunsorted[0]
    aminindex = 0
    for i in range(len(aunsorted)):
        if aunsorted[i] < amin:
            amin = aunsorted[i]
            aminindex = i
    del aunsorted[aminindex]
    asorted.append(amin)
print(asorted)