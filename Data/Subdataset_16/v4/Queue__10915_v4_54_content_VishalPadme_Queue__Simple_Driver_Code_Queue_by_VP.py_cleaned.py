import queue
def fonk1(b3):
    b1 = b3.qsize()
    for _ in range(b1):
        b2 = b3.get()
        print(b2)
        b3.put(b2)
def fonk2():
    b3 = queue.Queue()
    print("MENU:\n1. EnQueue\n2. DeQueue\n3. LengthOfQueue\n4. Check Queue Emptiness\n5. Display Queue\n6. EXIT")
    while True:
        b4 = int(input("Enter Your Choice: "))
        if b4 = = 1:
            b5 = int(input("Enter Element To Be Inserted Into Queue: "))
            b3.put(b5)
            print(f"Value {b5} Inserted")
        elif b4 = = 2:
            if b3.qsize() == 0:
                print("Queue Is Empty, Cannot Delete Element!")
            else:
                b6 = b3.get()
                print(f"Removed Element: {b6}")
        elif b4 = = 3:
            b7 = b3.qsize()
            print(f"Number Of Elements In The Queue: {b7}")
        elif b4 = = 4:
            if b3.qsize() == 0:
                print("Queue Is Empty")
            else:
                print("Queue Is Not Empty")
        elif b4 = = 5:
            fonk1(b3)
            print("End")
        elif b4 = = 6:
            print("Exiting...")
            break
        else:
            print("INVALID INPUT, Execution Stopped. YOU HAVE TO RUN AGAIN!")
            break
if b8 = = '__main__':
    fonk2()