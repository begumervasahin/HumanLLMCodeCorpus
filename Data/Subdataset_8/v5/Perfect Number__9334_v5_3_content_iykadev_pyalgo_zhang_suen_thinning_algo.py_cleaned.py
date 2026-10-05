from __future__ import division
from PIL import Image
beforeTxt = '''\
1100111
1100111
1100111
1100111
1100110
1100110
1100110
1100110
1100110
1100110
1100110
1100110
1111110
0000000\
'''
smallrc01 = '''\
00000000000000000000000000000000
01111111110000000111111110000000
01110001111000001111001111000000
01110000111000001110000111000000
01110001111000001110000000000000
01111111110000001110000000000000
01110111100000001110000111000000
01110011110011101111001111011100
01110001111011100111111110011100
00000000000000000000000000000000
'''
rc01 = '''\
00000000000000000000000000000000000000000000000000000000000
01111111111111111100000000000000000001111111111111000000000
01111111111111111110000000000000001111111111111111000000000
01111111111111111111000000000000111111111111111111000000000
01111111100000111111100000000001111111111111111111000000000
00011111100000111111100000000011111110000000111111000000000
000111111000001111111000000
from __future__ import division
from PIL import Image
def convert_to_int_array(binary_string):
    return [[int(char) for char in line] for line in binary_string.strip().split()]
def convert_to_binary_string(int_matrix):
    return '\n'.join(''.join(map(str, row)) for row in int_matrix)
def to_text(int_matrix):
    return '\n'.join(''.join(map(str, row)) for row in int_matrix)
def get_neighbours(x, y, image):
    img = image
    x1, y1, x_1, y_1 = x + 1, y - 1, x - 1, y + 1
    return [img[y1][x], img[y1][x1], img[y][x1], img[y_1][x1],
            img[y_1][x], img[y_1][x_1], img[y][x_1], img[y1][x_1]]
def count_transitions(neighbours):
    n = neighbours + neighbours[0:1]
    return sum((n1, n2) == (0, 1) for n1, n2 in zip(n, n[1:]))
def zhang_suen_thinning(image):
    changing1 = changing2 = [(-1, -1)]
    while changing1 or changing2:
        changing1 = []
        for y in range(1, len(image) - 1):
            for x in range(1, len(image[0]) - 1):
                P2, P3, P4, P5, P6, P7, P8, P9 = n = get_neighbours(x, y, image)
                if (image[y][x] == 1 and
                        P4 * P6 * P8 == 0 and
                        P2 * P4 * P6 == 0 and
                        count_transitions(n) == 1 and
                        2 <= sum(n) <= 6):
                    changing1.append((x, y))
        for x, y in changing1:
            image[y][x] = 0
        changing2 = []
        for y in range(1, len(image) - 1):
            for x in range(1, len(image[0]) - 1):
                P2, P3, P4, P5, P6, P7, P8, P9 = n = get_neighbours(x, y, image)
                if (image[y][x] == 1 and
                        P2 * P6 * P8 == 0 and
                        P2 * P4 * P8 == 0 and
                        count_transitions(n) == 1 and
                        2 <= sum(n) <= 6):
                    changing2.append((x, y))
        for x, y in changing2:
            image[y][x] = 0
    return image
if __name__ == '__main__':
    for picture in (beforeTxt, smallrc01, rc01):
        image = convert_to_int_array(picture)
        print('\nFrom:\n%s' % to_text(image))
        after = zhang_suen_thinning(image)
        print('\nTo thinned:\n%s' % to_text(after))