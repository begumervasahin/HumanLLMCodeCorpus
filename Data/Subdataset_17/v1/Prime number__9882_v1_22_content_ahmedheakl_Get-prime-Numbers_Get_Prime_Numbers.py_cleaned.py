def main():
    n = int(input('Enter the end of the range: '))
    a = []
    for i in range(1, 1000000000000000000):
        b = (24 * i + 1) ** 0.5
        if b % 1 == 0 and int(b) < n:
            a.append(int(b))
        elif int(b) >= n:
            break
    for i in range(2, 10):
        a = [z for z in a if z % i != 0]
    z = [y ** 2 for y in a]
    a = [hh for hh in a if hh not in z]
    aaa = [2, 3, 5, 7]
    a += aaa
    print(sorted(a))
if __name__ == "__main__":
    main()