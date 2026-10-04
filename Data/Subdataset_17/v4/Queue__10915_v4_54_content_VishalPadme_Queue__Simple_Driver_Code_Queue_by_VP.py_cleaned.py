import queue
def display_queue(q):
    size = q.qsize()
    for _ in range(size):
        element = q.get()
        print(element)
        q.put(element)
def main():
    q = queue.Queue()
    print("MENU:\n1. EnQueue\n2. DeQueue\n3. LengthOfQueue\n4. Check Queue Emptiness\n5. Display Queue\n6. EXIT")
    while True:
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            val = int(input("Enter Element To Be Inserted Into Queue: "))
            q.put(val)
            print(f"Value {val} Inserted")
        elif choice == 2:
            if q.qsize() == 0:
                print("Queue Is Empty, Cannot Delete Element!")
            else:
                removed_element = q.get()
                print(f"Removed Element: {removed_element}")
        elif choice == 3:
            length = q.qsize()
            print(f"Number Of Elements In The Queue: {length}")
        elif choice == 4:
            if q.qsize() == 0:
                print("Queue Is Empty")
            else:
                print("Queue Is Not Empty")
        elif choice == 5:
            display_queue(q)
            print("End")
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("INVALID INPUT, Execution Stopped. YOU HAVE TO RUN AGAIN!")
            break
if __name__ == '__main__':
    main()