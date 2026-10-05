import cProfile
def compute_golden_ratio_sequence(n):
    s = 1
    t = 1
    for i in range(2, n):
        c = s + t
        s = t
        t = c
        ratio = t / s
        print(ratio)
def main():
    n = 1476
    compute_golden_ratio_sequence(n)
if __name__ == "__main__":
    cProfile.run("main()", filename="profile_results.txt")