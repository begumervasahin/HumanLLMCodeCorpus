from b3 import Queue
def fonk1(b3):
    b1 = b3.qsize()
    while b1 > 0:
        b2 = b3.get()
        print("Item:", b2)
        b3.put(b2)
        b1 -= 1
b3 = Queue()
print("MENU:")
print("1. EnQueue")
print("2. DeQueue")
print("3. Length Of Queue")
print("4. Check Queue Emptiness")
print("5. Display Queue")
print("6. EXIT")
b4 = int(input("Enter Your Choice: "))
while b4 <= 5:
    if b4 = = 1:
        b5 = int(input("Enter Element To Be Inserted Into Queue: "))
        b3.put(b5)
        print("Value", b5, "Inserted")
    elif b4 = = 2:
        if b3.qsize() == 0:
            print("Queue Is Empty, Cannot Delete Element!!!")
        else:
            print("Removed Element:", b3.get())
    elif b4 = = 3:
        b6 = b3.qsize()
        print("Number Of Elements In The Queue Are:", b6)
    elif b4 = = 4:
        if b3.qsize() == 0:
            print("Queue Is Empty")
        else:
            print("Queue Is Not Empty")
    elif b4 = = 5:
        print("Displaying Queue:")
        fonk1(b3)
        print("End")
    b4 = int(input("Enter Your Next Choice: "))
print("INVALID INPUT, Execution Stopped")
print("YOU HAVE TO RUN AGAIN!!!!!!")