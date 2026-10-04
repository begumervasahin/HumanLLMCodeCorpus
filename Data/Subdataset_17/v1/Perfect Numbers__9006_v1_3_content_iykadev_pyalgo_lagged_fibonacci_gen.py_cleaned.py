def main():
    j = 3
    k = 7
    s = [8, 6, 7, 5, 3, 0, 9]
    for n in range(10):
        for i in range(len(s)):
            if i == 0:
                out = (s[j - 1] + s[k - 1]) % 10
            elif 0 < i < len(s) - 1:
                s[i] = s[i + 1]
            else:
                s[i] = out
                print(s[i])
if __name__ == "__main__":
    main()