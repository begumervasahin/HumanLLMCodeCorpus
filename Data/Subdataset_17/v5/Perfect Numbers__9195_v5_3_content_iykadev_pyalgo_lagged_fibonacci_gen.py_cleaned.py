def shift_and_replace(s, j, k, iterations=10):
    for n in range(iterations):
        for i in range(len(s)):
            if i == 0:
                out = (s[j - 1] + s[k - 1]) % 10
            elif 0 < i < len(s) - 1:
                s[i] = s[i + 1]
            else:
                s[i] = out
                print(s[i])
    return s
def main():
    initial_list = [8, 6, 7, 5, 3, 0, 9]
    j = 3
    k = 7
    result = shift_and_replace(initial_list, j, k)
    print(f"Final list: {result}")
if __name__ == "__main__":
    main()