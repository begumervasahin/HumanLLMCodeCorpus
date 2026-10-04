def spiral(n):
    def spiral_part(x, y, n):
        if x == -1 and y == 0:
            return -1
        if y == (x + 1) and x < (n
            return spiral_part(x - 1, y - 1, n - 1) + 4 * (n - y)
        if x < (n - y) and y <= x:
            return spiral_part(y - 1, y, n) + (x - y) + 1
        if x >= (n - y) and y <= x:
            return spiral_part(x, y - 1, n) + 1
        if x >= (n - y) and y > x:
            return spiral_part(x + 1, y, n) + 1
        if x < (n - y) and y > x:
            return spiral_part(x, y - 1, n) - 1
    array = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            array[x][y] = spiral_part(y, x, n)
    return array
def print_spiral(matrix):
    for row in matrix:
        print(" ".join("{:2}".format(x) for x in row))
if __name__ == "__main__":
    size = 6
    spiral_matrix = spiral(size)
    print_spiral(spiral_matrix)