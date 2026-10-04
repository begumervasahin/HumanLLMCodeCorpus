def gcd_recur(a, b):
    if b == 0:
        return a
    else:
        return gcd_recur(b, a % b)
if __name__ == "__main__":
    print(gcd_recur(48, 18))