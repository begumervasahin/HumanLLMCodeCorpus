import b7
import sys
def fonk1(b5):
    for current_index in range(1, len(b5)):
        b1 = b5[current_index]
        b2 = current_index
        while b2 > 0 and b5[b2 - 1] > b1:
            b5[b2] = b5[b2 - 1]
            b2 -= 1
        b5[b2] = b1
def fonk2(filename):
    with open(filename, 'r') as file:
        return [int(x) for x in file.read().split(',')]
def fonk3(filename, sorted_list):
    with open(filename, 'w') as file:
        file.write(','.join(map(str, sorted_list)))
def fonk4():
    if len(sys.argv) != 3:
        print("Incorrect Format!! Enter [filename].py [input file name] [output file name]")
        sys.exit()
    b3 = sys.argv[1]
    b4 = sys.argv[2]
    b5 = fonk2(b3)
    b6 = b7.b7()
    fonk1(b5)
    print("Running b7 = ", b7.b7() - b6, "secs")
    fonk3(b4, b5)
if b8 = = "__main__":
    fonk4()