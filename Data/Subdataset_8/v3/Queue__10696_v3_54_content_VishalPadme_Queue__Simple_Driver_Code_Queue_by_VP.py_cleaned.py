from queue import Queue
def display_queue(queue):
    size = queue.qsize()
    while size > 0:
        item = queue.get()
        print("Item:", item)
        queue.put(item)
        size -= 1
def main_menu():
    print("MENU:")
    print("1. EnQueue")
    print("2. DeQueue")
    print("3. Length Of Queue")
    print("4. Check Queue Emptiness")
    print("5. Display Queue")
    print("6. EXIT")
def handle_enqueue(queue):
    value = int(input("Enter Element To Be Inserted Into Queue: "))
    queue.put(value)
    print("Value", value, "Inserted")
def handle_dequeue(queue):
    if queue.qsize() == 0:
        print("Queue Is Empty, Cannot Delete Element!!!")
    else:
        print("Removed Element:", queue.get())
def handle_length(queue):
    length = queue.qsize()
    print("Number Of Elements In The Queue Are:", length)
def handle_emptiness(queue):
    if queue.qsize() == 0:
        print("Queue Is Empty")
    else:
        print("Queue Is Not Empty")
if __name__ == "__main__":
    queue = Queue()
    while True:
        main_menu()
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            handle_enqueue(queue)
        elif choice == 2:
            handle_dequeue(queue)
        elif choice == 3:
            handle_length(queue)
        elif choice == 4:
            handle_emptiness(queue)
        elif choice == 5:
            print("Displaying Queue:")
            display_queue(queue)
            print("End")
        elif choice == 6:
            print("Exiting Program...")
            break
        else:
            print("INVALID INPUT! Please enter a valid choice.")