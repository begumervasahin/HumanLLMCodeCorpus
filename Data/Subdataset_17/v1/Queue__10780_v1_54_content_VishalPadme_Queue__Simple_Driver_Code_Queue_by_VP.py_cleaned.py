import queue
def display_queue(q):
    s = q.qsize()
    temp_queue = queue.Queue()
    while s > 0:
        item = q.get()
        print(item)
        temp_queue.put(item)
        s -= 1
    while not temp_queue.empty():
        q.put(temp_queue.get())
def main():
    q = queue.Queue()
    print("MENU:\n1. EnQueue\n2. DeQueue\n3. Length Of Queue\n4. Check Queue Emptiness\n5. Display Queue\n6. EXIT")
    while True:
        try:
            ch = int(input("Enter Your Choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.")
            continue
        if ch == 1:
            try:
                val = int(input("Enter Element To Be Inserted Into Queue: "))
                q.put(val)
                print(f"Value {val} Inserted")
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
        elif ch == 2:
            if q.empty():
                print("Queue Is Empty, Cannot Delete Element!")
            else:
                print(f"Removed Element: {q.get()}")
        elif ch == 3:
            l = q.qsize()
            print(f"Number Of Elements In The Queue: {l}")
        elif ch == 4:
            if q.empty():
                print("Queue Is Empty")
            else:
                print("Queue Is Not Empty")
        elif ch == 5:
            display_queue(q)
            print("End of Display")
        elif ch == 6:
            print("Exiting the program.")
            break
        else:
            print("INVALID INPUT, Execution Stopped. YOU HAVE TO RUN AGAIN!!!!!!")
if __name__ == '__main__':
    main()