def transform_list(s: list, j: int, k: int, iterations: int) -> None:
    for _ in range(iterations):
        for i in range(len(s)):
            if i == 0:
                new_value = (s[j - 1] + s[k - 1]) % 10
            elif 0 < i < len(s) - 1:
                s[i] = s[i + 1]
            else:
                s[i] = new_value
                print(s[i])
def main() -> None:
    j = 3
    k = 7
    s = [8, 6, 7, 5, 3, 0, 9]
    iterations = 10
    print("Original list:", s)
    transform_list(s, j, k, iterations)
    print("Transformed list:", s)
if __name__ == "__main__":
    main()