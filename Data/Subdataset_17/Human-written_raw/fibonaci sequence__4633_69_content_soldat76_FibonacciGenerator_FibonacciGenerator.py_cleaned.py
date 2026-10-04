print("\nThis program will print out a Fibonacci sequence of your desired length!")
def printSequence():
    print("\nHere is your Fibonacci sequence of %i number(s): \n\t%s" %(length,fibonacciStart))
x = 1
while x == 1:
    fibonacciStart = [1,1]
    length = int(input("\nEnter your desired Fibonacci sequence length: "))
    fibonacciStart = [1,1]
    if length <= 0:
        print("The sequence must contain some positive number.")
    if length == 2:
        fibonacciStart = [1,1]
        printSequence()
    if length == 1:
        fibonacciStart = [1]
        printSequence()
    if length >2:
        for i in range(length):
            addNext = int((fibonacciStart[(len(fibonacciStart)- 2)]) + (fibonacciStart[(len(fibonacciStart) - 1)]))
            fibonacciStart.append(addNext)
            if len(fibonacciStart) == length:
                break
        printSequence()