import queue
def fonk1(b4):
    b1 = queue.Queue()
    b2 = b4.qsize()
    while b2 > 0:
        b3 = b4.get()
        print(b3)
        b1.put(b3)
        b2 -= 1
    while not b1.empty():
        b4.put(b1.get())
def fonk2():
    b4 = queue.Queue()
    b5 = print(b5)
    while True:
        try:
            b6 = int(input("Enter Your Choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.")
            continue
        if b6 = = 1:
            try:
                b7 = int(input("Enter Element To Be Inserted Into Queue: "))
                b4.put(b7)
                print(f"Value {b7} Inserted")
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
        elif b6 = = 2:
            if b4.empty():
                print("Queue Is Empty, Cannot Delete Element!")
            else:
                print(f"Removed Element: {b4.get()}")
        elif b6 = = 3:
            b8 = b4.qsize()
            print(f"Number Of Elements In The Queue: {b8}")
        elif b6 = = 4:
            if b4.empty():
                print("Queue Is Empty")
            else:
                print("Queue Is Not Empty")
        elif b6 = = 5:
            fonk1(b4)
            print("End of Display")
        elif b6 = = 6:
            print("Exiting the program.")
            break
        else:
            print("INVALID INPUT. Please enter a number between 1 and 6.")
if b9 = = '__main__':
    fonk2()