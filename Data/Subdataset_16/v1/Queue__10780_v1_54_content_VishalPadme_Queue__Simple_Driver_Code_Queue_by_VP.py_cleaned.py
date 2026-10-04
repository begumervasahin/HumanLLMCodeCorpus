import queue
def fonk1(b4):
    b1 = b4.qsize()
    b2 = queue.Queue()
    while b1 > 0:
        b3 = b4.get()
        print(b3)
        b2.put(b3)
        b1 -= 1
    while not b2.empty():
        b4.put(b2.get())
def fonk2():
    b4 = queue.Queue()
    print("MENU:\n1. EnQueue\n2. DeQueue\n3. Length Of Queue\n4. Check Queue Emptiness\n5. Display Queue\n6. EXIT")
    while True:
        try:
            b5 = int(input("Enter Your Choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.")
            continue
        if b5 = = 1:
            try:
                b6 = int(input("Enter Element To Be Inserted Into Queue: "))
                b4.put(b6)
                print(f"Value {b6} Inserted")
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
        elif b5 = = 2:
            if b4.empty():
                print("Queue Is Empty, Cannot Delete Element!")
            else:
                print(f"Removed Element: {b4.get()}")
        elif b5 = = 3:
            b7 = b4.qsize()
            print(f"Number Of Elements In The Queue: {b7}")
        elif b5 = = 4:
            if b4.empty():
                print("Queue Is Empty")
            else:
                print("Queue Is Not Empty")
        elif b5 = = 5:
            fonk1(b4)
            print("End of Display")
        elif b5 = = 6:
            print("Exiting the program.")
            break
        else:
            print("INVALID INPUT, Execution Stopped. YOU HAVE TO RUN AGAIN!!!!!!")
if b8 = = '__main__':
    fonk2()