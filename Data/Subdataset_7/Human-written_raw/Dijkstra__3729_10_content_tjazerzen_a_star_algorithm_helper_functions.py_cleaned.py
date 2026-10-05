from math import sqrt
def fonk1(b4, b5, b7, b8):
    b1 = (b4 - b7)**2
    b2 = (b5 - b8)**2
    b3 = sqrt(b1 + b2)
    return b3
def fonk2(end_point, coordinates):
    b4 = coordinates[end_point][0]
    b5 = coordinates[end_point][1]
    b6 = []
    for i in range(len(coordinates)):
        b7 = coordinates[i][0]
        b8 = coordinates[i][1]
        b3 = fonk1(b4, b5, b7, b8)
        b6.append(b3)
    return b6
def fonk3(coordinates, connection_list):
    b6 = connection_list
    for i in range(len(connection_list)):
        for j in range(len(connection_list[i])):
            b9 = i
            b10 = connection_list[i][j]
            b4 = coordinates[b9][0]
            b5 = coordinates[b9][1]
            b7 = coordinates[b10][0]
            b8 = coordinates[b10][1]
            b3 = fonk1(b4, b5, b7, b8)
            b6[i][j] = b3
    return b6