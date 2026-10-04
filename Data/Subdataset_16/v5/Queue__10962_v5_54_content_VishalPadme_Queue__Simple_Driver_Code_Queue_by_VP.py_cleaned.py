import queue
def fonk1(b6):
    b1 = b6.qsize()
    for _ in range(b1):
        b2 = b6.get()
        print(b2)
        b6.put(b2)
def fonk2(b6):
    b3 = int(input("Enter Element To Be Inserted Into Queue: "))
    b6.put(b3)
    print(f"Value {b3} Inserted")
def fonk3(b6):
    if b6.empty():
        print("Queue Is Empty, Cannot Delete Element!")
    else:
        b4 = b6.get()
        print(f"Removed Element: {b4}")
def fonk4(b6):
    b5 = b6.qsize()
    print(f"Number Of Elements In The Queue: {b5}")
def fonk5(b6):
    if b6.empty():
        print("Queue Is Empty")
    else:
        print("Queue Is Not Empty")
def fonk6():
    b6 = queue.Queue()
    b7 = (
        "MENU:\n"
        "1. EnQueue\n"
        "2. DeQueue\n"
        "3. Length Of Queue\n"
        "4. Check Queue Emptiness\n"
        "5. Display Queue\n"
        "6. EXIT"
    )
    print(b7)
    b8 = {
        1: enqueue,
        2: dequeue,
        3: length_of_queue,
        4: check_emptiness,
        5: display_queue
    }
    while True:
        try:
            b9 = int(input("Enter Your Choice: "))
        except ValueError:
            print("Invalid input, please enter a number between 1 and 6.")
            continue
        if b9 = = 6:
            print("Exiting...")
            break
        elif b9 in b8:
            b8[b9](b6)
        else:
            print("Invalid b9, please enter a number between 1 and 6.")
if b10 = = '__main__':
    fonk6()