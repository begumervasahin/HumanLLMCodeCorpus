class Sorting:
    def __init__(self):
        self.listOfNumbers = []
    def addNumber(self, number):
        self.listOfNumbers.append(number)
    def returnList(self):
        return self.listOfNumbers
    def printEachElementOfList(self):
        for number in self.listOfNumbers:
            print(number)
    def quickSort(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[len(arr) - 1]
            lessThanPivot = [number for number in arr if number < pivot]
            equalPivot = [number for number in arr if number == pivot]
            greaterThanPivot = [number for number in arr if number > pivot]
            return self.quickSort(lessThanPivot) + equalPivot + self.quickSort(greaterThanPivot)
if __name__ == "__main__":
    sorting = Sorting()
    numbers_to_add = [34, 7, 23, 32, 5, 62, 32, 7]
    for number in numbers_to_add:
        sorting.addNumber(number)
    print("Original list:")
    sorting.printEachElementOfList()
    sorted_list = sorting.quickSort(sorting.returnList())
    print("\nSorted list:")
    for number in sorted_list:
        print(number)