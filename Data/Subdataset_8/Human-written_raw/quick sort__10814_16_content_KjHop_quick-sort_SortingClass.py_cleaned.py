class Sorting:
    listOfNumbers = []
    def addNumber(self,number):
        self.listOfNumbers.append(number)
    def returnList(self):
        return self.listOfNumbers
    def printEachElementOfList(self):
        for number in self.listOfNumbers:
            print(number)
    def quickSort(self, arr):
        lessThanPivot = []
        equalPivot = []
        greaterThanPivot = []
        if len(arr)>1:
            pivot = arr[len(arr)-1]
            for number in arr:
                if number < pivot:
                    lessThanPivot.append(number)
                elif number == pivot:
                    equalPivot.append(number)
                else:
                    greaterThanPivot.append(number)
            return self.quickSort(lessThanPivot)+equalPivot+self.quickSort(greaterThanPivot)
        else:
            return arr