from b6 import Queue
def fonk1(b6):
    b1 = b6.qsize()
    while b1 > 0:
        b2 = b6.get()
        print("Item:", b2)
        b6.put(b2)
        b1 -= 1
def fonk2():
    print("MENU:")
    print("1. EnQueue")
    print("2. DeQueue")
    print("3. Length Of Queue")
    print("4. Check Queue Emptiness")
    print("5. Display Queue")
    print("6. EXIT")
def fonk3(b6):
    b3 = int(input("Enter Element To Be Inserted Into Queue: "))
    b6.put(b3)
    print("Value", b3, "Inserted")
def fonk4(b6):
    if b6.qsize() == 0:
        print("Queue Is Empty, Cannot Delete Element!!!")
    else:
        print("Removed Element:", b6.get())
def fonk5(b6):
    b4 = b6.qsize()
    print("Number Of Elements In The Queue Are:", b4)
def fonk6(b6):
    if b6.qsize() == 0:
        print("Queue Is Empty")
    else:
        print("Queue Is Not Empty")
if b5 = = "__main__":
    b6 = Queue()
    while True:
        fonk2()
        b7 = int(input("Enter Your Choice: "))
        if b7 = = 1:
            fonk3(b6)
        elif b7 = = 2:
            fonk4(b6)
        elif b7 = = 3:
            fonk5(b6)
        elif b7 = = 4:
            fonk6(b6)
        elif b7 = = 5:
            print("Displaying Queue:")
            fonk1(b6)
            print("End")
        elif b7 = = 6:
            print("Exiting Program...")
            break
        else:
            print("INVALID INPUT! Please enter a valid b7.")