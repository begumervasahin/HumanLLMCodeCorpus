import sys
num_recursive_calls = 0
def recursive_lcs(x, y, reconstruct=False):
    global num_recursive_calls
    num_recursive_calls += 1
    if not x or not y:
        return "" if reconstruct else 0
    if x[-1] == y[-1]:
        if reconstruct:
            return recursive_lcs(x[:-1], y[:-1], reconstruct) + x[-1]
        else:
            return 1 + recursive_lcs(x[:-1], y[:-1], reconstruct)
    else:
        if reconstruct:
            return max(recursive_lcs(x, y[:-1], reconstruct),
                       recursive_lcs(x[:-1], y, reconstruct), key=len)
        else:
            return max(recursive_lcs(x, y[:-1], reconstruct),
                       recursive_lcs(x[:-1], y, reconstruct))
def test(x, y, reconstruct):
    return recursive_lcs(x, y, reconstruct)
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 {} <filename> <reconstruct_flag>".format(sys.argv[0]))
        print("<filename>: name of the file containing sequences")
        print("<reconstruct_flag>: 0 - without reconstruction, 1 - with reconstruction")
    else:
        filename = sys.argv[1]
        reconstruct = len(sys.argv) == 3 and int(sys.argv[2]) == 1
        with open(filename, 'r') as f:
            x = f.readline().strip()
            y = f.readline().strip()
            lcs = test(x, y, reconstruct)
            print("LCS: " + lcs if reconstruct else "LCS length: " + str(lcs))
            print("Number of recursive calls: " + str(num_recursive_calls))