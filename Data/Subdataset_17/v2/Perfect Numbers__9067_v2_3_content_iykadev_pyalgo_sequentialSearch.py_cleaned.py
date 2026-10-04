def sequential_search(arr: list, target: any) -> bool:
    pos = 0
    found = False
    while pos < len(arr) and not found:
        if arr[pos] == target:
            found = True
        else:
            pos += 1
    return found
def main() -> None:
    test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(sequential_search(test_list, 3))
    print(sequential_search(test_list, 13))
if __name__ == "__main__":
    main()