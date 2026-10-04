def spiral(n):
    def fill_spiral(x, y, n):
        if x == -1 and y == 0:
            return -1
        if y == x + 1 and x < n
            return fill_spiral(x - 1, y - 1, n - 1) + 4 * (n - y)
        if x < n - y and y <= x:
            return fill_spiral(y - 1, y, n) + (x - y) + 1
        if x >= n - y and y <= x:
            return fill_spiral(x, y - 1, n) + 1
        if x >= n - y and y > x:
            return fill_spiral(x + 1, y, n) + 1
        if x < n - y and y > x:
            return fill_spiral(x, y - 1, n) - 1
    matrix = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            matrix[x][y] = fill_spiral(y, x, n)
    return matrix
def print_spiral(matrix):
    for row in matrix:
        print(" ".join("{:2}".format(x) for x in row))
if __name__ == "__main__":
    size = 6
    spiral_matrix = spiral(size)
    print_spiral(spiral_matrix)