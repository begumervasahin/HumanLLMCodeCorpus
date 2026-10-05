def intarray(binstring):
    '''Converts a 2D matrix of 01 chars into a list of lists of ints'''
    return [[1 if ch == '1' else 0 for ch in line] for line in binstring.strip().split()]
def chararray(intmatrix):
    '''Converts a 2D list of lists of 1/0 ints into lines of 1/0 chars'''
    return '\n'.join(''.join(str(p) for p in row) for row in intmatrix)
def toTxt(intmatrix):
    '''Converts a 2D list of lists of 1/0 ints into lines of 01 chars'''
    return '\n'.join(''.join(('1' if pixel == 1 else '0') for pixel in row) for row in intmatrix)
def neighbours(x, y, image):
    '''Returns 8-neighbours of point (x, y) in the image'''
    i = image
    x1, y1, x_1, y_1 = x+1, y-1, x-1, y+1
    return [i[y1][x],  i[y1][x1],   i[y][x1],  i[y_1][x1],
            i[y_1][x], i[y_1][x_1], i[y][x_1], i[y1][x_1]]
def transitions(neighbours):
    '''Returns the number of transitions from 0 to 1 in the 8-neighbours'''
    n = neighbours + neighbours[0:1]
    return sum((n1, n2) == (0, 1) for n1, n2 in zip(n, n[1:]))
def zhangSuen(image):
    '''Applies Zhang-Suen thinning algorithm to the input binary image'''
    changing1 = changing2 = [(-1, -1)]
    while changing1 or changing2:
        changing1 = []
        for y in range(1, len(image) - 1):
            for x in range(1, len(image[0]) - 1):
                P2, P3, P4, P5, P6, P7, P8, P9 = n = neighbours(x, y, image)
                if (image[y][x] == 1 and
                    P4 * P6 * P8 == 0 and
                    P2 * P4 * P6 == 0 and
                    transitions(n) == 1 and
                    2 <= sum(n) <= 6):
                    changing1.append((x,y))
        for x, y in changing1:
            image[y][x] = 0
        changing2 = []
        for y in range(1, len(image) - 1):
            for x in range(1, len(image[0]) - 1):
                P2, P3, P4, P5, P6, P7, P8, P9 = n = neighbours(x, y, image)
                if (image[y][x] == 1 and
                    P2 * P6 * P8 == 0 and
                    P2 * P4 * P8 == 0 and
                    transitions(n) == 1 and
                    2 <= sum(n) <= 6):
                    changing2.append((x,y))
        for x, y in changing2:
            image[y][x] = 0
    return image
if __name__ == '__main__':
    for picture in (beforeTxt, smallrc01, rc01):
        image = intarray(picture)
        print('\nFrom:\n%s' % toTxt(image))
        after = zhangSuen(image)
        print('\nTo thinned:\n%s' % toTxt(after))