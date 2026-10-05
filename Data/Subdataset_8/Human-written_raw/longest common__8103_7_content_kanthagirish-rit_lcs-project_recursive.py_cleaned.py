
import sys
num_recursive_calls = 0
def recursive_lcs(x, y, reconstruct=False):
    global num_recursive_calls
    num_recursive_calls += 1
    if len(x) == 0 or len(y) == 0:
        if reconstruct:
            return ""
        else:
            return 0
    if x[-1] == y[-1]:
        if reconstruct:
            return recursive_lcs(x[:-1], y[:-1], reconstruct) + x[-1]
        else:
            return 1 + recursive_lcs(x[:-1], y[:-1], reconstruct)
    else:
        if reconstruct:
            return max(recursive_lcs(x, y[:-1], reconstruct)
                       , recursive_lcs(x[:-1], y, reconstruct), key=len)
        else:
            return max(recursive_lcs(x, y[:-1], reconstruct)
                       , recursive_lcs(x[:-1], y, reconstruct))
def test(x, y, reconstruct):
    return recursive_lcs(x, y, reconstruct)
if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Usage: python3 " + __file__ + " acgt/bits")
        print("acgt - generate sequences of acgt")
        print("bits- generate sequences of binary digits")
        print("0 - without reconstruction, 1 - with reconstruction")
    else:
        file = sys.argv[1] + ".txt"
        with open(file, 'r') as f:
            x = f.readline().strip()
            y = f.readline().strip()
            reconstruct = False
            if len(sys.argv) == 3:
                reconstruct = int(sys.argv[2]) == 1
            if reconstruct:
                lcs = test(x, y, reconstruct)
                print("LCS: " + lcs)
                print("LCS length: " + str(len(lcs)))
            else:
                print("LCS length: " + str(test(x, y, reconstruct)))
            print("Number of recursive calls: " + str(num_recursive_calls))