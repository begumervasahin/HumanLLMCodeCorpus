from random import randint
def insertion_sort(arr):
    for index in range(1, len(arr)):
        current = arr[index]
        position = index
        while position > 0 and arr[position - 1] > current:
            print("Swapped {} for {}".format(arr[position], arr[position - 1]))
            arr[position] = arr[position - 1]
            print(arr)
            print("===================================================================================================")
            position -= 1
        arr[position] = current
    return arr
def generate_random_array():
    array = []
    num_elements = int(input("Enter the number of elements: "))
    for _ in range(num_elements):
        item = randint(1, 100)
        if item in array:
            continue
        array.append(item)
    return array
def main():
    arr = generate_random_array()
    print("List to be sorted using INSERTION SORT: {}".format(arr))
    insertion_sort(arr)
    print("Final Sorted List: {}".format(arr))
if __name__ == "__main__":
    main()