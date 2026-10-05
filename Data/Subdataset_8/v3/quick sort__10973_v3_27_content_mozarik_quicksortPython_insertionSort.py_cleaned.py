from random import randint
def insertion_sort(arr):
    for index in range(1, len(arr)):
        current = arr[index]
        position = index
        while position > 0 and arr[position - 1] > current:
            arr[position] = arr[position - 1]
            position -= 1
        arr[position] = current
    return arr
def generate_random_array():
    array = []
    num_elements = int(input("Enter the number of elements: "))
    for _ in range(num_elements):
        item = randint(1, 100)
        if item not in array:
            array.append(item)
    return array
def main():
    arr = generate_random_array()
    print("List to be sorted using INSERTION SORT:", arr)
    sorted_arr = insertion_sort(arr.copy())
    print("Final Sorted List:", sorted_arr)
if __name__ == "__main__":
    main()