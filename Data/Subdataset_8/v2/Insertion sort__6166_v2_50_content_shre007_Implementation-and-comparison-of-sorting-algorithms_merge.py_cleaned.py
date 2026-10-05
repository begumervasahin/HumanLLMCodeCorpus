def merge_sort(given_list):
    if len(given_list) > 1:
        mid = len(given_list)
        left_list = given_list[:mid]
        right_list = given_list[mid:]
        merge_sort(left_list)
        merge_sort(right_list)
        i = j = k = 0
        while len(left_list) > i and len(right_list) > j:
            if left_list[i] < right_list[j]:
                given_list[k] = left_list[i]
                i += 1
            else:
                given_list[k] = right_list[j]
                j += 1
            k += 1
        while len(left_list) > i:
            given_list[k] = left_list[i]
            i += 1
            k += 1
        while len(right_list) > j:
            given_list[k] = right_list[j]
            j += 1
            k += 1
number_of_elements = int(input("How many elements do you want in this list: "))
given_list = [int(input("Enter element: ")) for _ in range(number_of_elements)]
merge_sort(given_list)
print("Sorted list:", given_list)