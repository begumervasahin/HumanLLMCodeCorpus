def sequential_search(arr: list, target: any) -> bool:
    for item in arr:
        if item == target:
            return True
    return False
def main() -> None:
    test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(f"Is 3 in the list? {sequential_search(test_list, 3)}")
    print(f"Is 13 in the list? {sequential_search(test_list, 13)}")
if __name__ == "__main__":
    main()