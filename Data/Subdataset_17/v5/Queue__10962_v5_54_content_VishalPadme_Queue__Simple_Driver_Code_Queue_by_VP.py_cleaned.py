import queue
def display_queue(q):
    size = q.qsize()
    for _ in range(size):
        element = q.get()
        print(element)
        q.put(element)
def enqueue(q):
    val = int(input("Enter Element To Be Inserted Into Queue: "))
    q.put(val)
    print(f"Value {val} Inserted")
def dequeue(q):
    if q.empty():
        print("Queue Is Empty, Cannot Delete Element!")
    else:
        removed_element = q.get()
        print(f"Removed Element: {removed_element}")
def length_of_queue(q):
    length = q.qsize()
    print(f"Number Of Elements In The Queue: {length}")
def check_emptiness(q):
    if q.empty():
        print("Queue Is Empty")
    else:
        print("Queue Is Not Empty")
def main():
    q = queue.Queue()
    menu = (
        "MENU:\n"
        "1. EnQueue\n"
        "2. DeQueue\n"
        "3. Length Of Queue\n"
        "4. Check Queue Emptiness\n"
        "5. Display Queue\n"
        "6. EXIT"
    )
    print(menu)
    actions = {
        1: enqueue,
        2: dequeue,
        3: length_of_queue,
        4: check_emptiness,
        5: display_queue
    }
    while True:
        try:
            choice = int(input("Enter Your Choice: "))
        except ValueError:
            print("Invalid input, please enter a number between 1 and 6.")
            continue
        if choice == 6:
            print("Exiting...")
            break
        elif choice in actions:
            actions[choice](q)
        else:
            print("Invalid choice, please enter a number between 1 and 6.")
if __name__ == '__main__':
    main()