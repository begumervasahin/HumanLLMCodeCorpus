def binary_string_to_matrix(bin_string):
    return [[1 if ch == '1' else 0 for ch in line] for line in bin_string.strip().split()]
def matrix_to_binary_string(int_matrix):
    return '\n'.join(''.join(str(pixel) for pixel in row) for row in int_matrix)
def matrix_to_txt(int_matrix):
    return '\n'.join(''.join(('1' if pixel == 1 else '0') for pixel in row) for row in int_matrix)
def get_neighbours(x, y, image):
    i = image
    x1, y1, x_1, y_1 = x + 1, y - 1, x - 1, y + 1
    return [i[y1][x], i[y1][x1], i[y][x1], i[y_1][x1],
            i[y_1][x], i[y_1][x_1], i[y][x_1], i[y1][x_1]]
def count_transitions(neighbours):
    n = neighbours + neighbours[0:1]
    return sum((n1, n2) == (0, 1) for n1, n2 in zip(n, n[1:]))
def zhang_suen_thinning(image):
    changing1 = changing2 = [(-1, -1)]
    while changing1 or changing2:
        changing1 = []
        for y in range(1, len(image) - 1):
            for x in range(1, len(image[0]) - 1):
                P2, P3, P4, P5, P6, P7, P8, P9 = get_neighbours(x, y, image)
                if (image[y][x] == 1 and
                    P4 * P6 * P8 == 0 and
                    P2 * P4 * P6 == 0 and
                    count_transitions(get_neighbours(x, y, image)) == 1 and
                    2 <= sum(get_neighbours(x, y, image)) <= 6):
                    changing1.append((x, y))
        for x, y in changing1:
            image[y][x] = 0
        changing2 = []
        for y in range(1, len(image) - 1):
            for x in range(1, len(image[0]) - 1):
                P2, P3, P4, P5, P6, P7, P8, P9 = get_neighbours(x, y, image)
                if (image[y][x] == 1 and
                    P2 * P6 * P8 == 0 and
                    P2 * P4 * P8 == 0 and
                    count_transitions(get_neighbours(x, y, image)) == 1 and
                    2 <= sum(get_neighbours(x, y, image)) <= 6):
                    changing2.append((x, y))
        for x, y in changing2:
            image[y][x] = 0
    return image
if __name__ == '__main__':
    for picture in (beforeTxt, smallrc01, rc01):
        image = binary_string_to_matrix(picture)
        print('\nFrom:\n%s' % matrix_to_txt(image))
        after = zhang_suen_thinning(image)
        print('\nTo thinned:\n%s' % matrix_to_txt(after))