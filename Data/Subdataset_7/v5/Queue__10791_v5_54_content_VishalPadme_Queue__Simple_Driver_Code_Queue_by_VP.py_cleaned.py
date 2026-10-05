import queue
def fonk1(b3):
    b1 = b3.qsize()
    while b1 > 0:
        b2 = b3.get()
        print(b2)
        b3.put(b2)
        b1 -= 1
def fonk2():
    b3 = queue.Queue()
    print("MENU:\n1. Enqueue\n2. Dequeue\n3. Length of Queue\n4. Check Queue Emptiness\n5. Display Queue\n6. EXIT")
    while True:
        b4 = int(input("Enter Your Choice: "))
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
            print("Number Of Elements In The Queue:", b6)
        elif b4 = = 4:
            if b3.qsize() == 0:
                print("Queue Is Empty")
            else:
                print("Queue Is Not Empty")
        elif b4 = = 5:
            fonk1(b3)
            print("End")
        elif b4 = = 6:
            print("Exiting the program...")
            break
        else:
            print("Invalid b4! Please enter a valid option.")
if b7 = = "__main__":
    fonk2()