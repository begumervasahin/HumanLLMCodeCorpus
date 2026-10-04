import queue
def display_queue(q):
    temp_queue = queue.Queue()
    size = q.qsize()
    while size > 0:
        item = q.get()
        print(item)
        temp_queue.put(item)
        size -= 1
    while not temp_queue.empty():
        q.put(temp_queue.get())
def main():
    q = queue.Queue()
    menu =
    print(menu)
    while True:
        try:
            choice = int(input("Enter Your Choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.")
            continue
        if choice == 1:
            try:
                val = int(input("Enter Element To Be Inserted Into Queue: "))
                q.put(val)
                print(f"Value {val} Inserted")
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
        elif choice == 2:
            if q.empty():
                print("Queue Is Empty, Cannot Delete Element!")
            else:
                removed_element = q.get()
                print(f"Removed Element: {removed_element}")
        elif choice == 3:
            length = q.qsize()
            print(f"Number Of Elements In The Queue: {length}")
        elif choice == 4:
            if q.empty():
                print("Queue Is Empty")
            else:
                print("Queue Is Not Empty")
        elif choice == 5:
            display_queue(q)
            print("End of Display")
        elif choice == 6:
            print("Exiting the program.")
            break
        else:
            print("INVALID INPUT. Please enter a number between 1 and 6.")
if __name__ == '__main__':
    main()