
def fonk1(array):
    for i in range(1, len(array)):
        b1 = i - 1
        b2 = array[i]
        while b1 >= 0 and array[b1] > b2:
            array[b1 + 1] = array[b1]
            b1 -= 1
        array[b1 + 1] = b2
if b3 = = "__main__":
    b4 = []
    with open("b6.txt", "r") as input_file:
        for line in input_file:
            b5 = []
            b6 = line.split()
            b6.pop(0)
            for number in b6:
                b5.append(int(number))
            b4.append(b5)
    for x in b4:
        fonk1(x)
    with open("insertionsort.txt", "w+") as output_file:
        for x in b4:
            for y in x:
                output_file.write("%i " % y)
            output_file.write("\n")