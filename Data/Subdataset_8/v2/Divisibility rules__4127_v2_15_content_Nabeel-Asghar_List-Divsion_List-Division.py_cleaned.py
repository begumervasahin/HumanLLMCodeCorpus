def division_function(list_a, list_b, threshold):
    result = []
    for num_a in list_a:
        count = 0
        for num_b in list_b:
            if num_a % num_b == 0:
                count += 1
        if count >= threshold:
            result.append(num_a)
    return set(result)
def main():
    input_list_a = input("Enter a list of numbers separated by a space: ")
    list_a = list(map(int, input_list_a.split()))
    input_list_b = input("Enter another list of numbers separated by a space: ")
    list_b = list(map(int, input_list_b.split()))
    threshold = len(list_b)
    result = division_function(list_a, list_b, threshold)
    print(result)
    input("Press Enter to exit.")
if __name__ == "__main__":
    main()