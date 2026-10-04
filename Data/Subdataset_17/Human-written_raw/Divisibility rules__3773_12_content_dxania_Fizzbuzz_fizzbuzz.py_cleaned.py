def get_input():
    list1 = [n for n in input("Enter the first list (separate elements with commas): ").split(",")]
    print(list1)
    print ("List1 is " + str(len(list1)) + " characters long")
    list2 = [n for n in input("Enter the second list (separate elements with commas): ").split(",")]
    print(list2)
    print ("List2 is " + str(len(list2)) + " characters long")
    print(Fizzbuzz(list1, list2))
def Fizzbuzz(a, b):
    totallength = len(a) + len(b)
    if totallength % 3 == 0:
        return 'Fizz'
    elif totallength % 5 == 0:
        return 'Buzz'
    elif totallength % 5 == 0 and totallength % 3 == 0:
        return 'FizzBuzz'
    else:
        return totallength
get_input()