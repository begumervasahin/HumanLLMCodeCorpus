import queue
def display_queue(q):
    size = q.qsize()
    while size > 0:
        element = q.get()
        print(element)
        q.put(element)
        size -= 1
def main():
    q = queue.Queue()
    print("MENU:\n1. Enqueue\n2. Dequeue\n3. Length of Queue\n4. Check Queue Emptiness\n5. Display Queue\n6. EXIT")
    while True:
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            value = int(input("Enter Element To Be Inserted Into Queue: "))
            q.put(value)
            print("Value", value, "Inserted")
        elif choice == 2:
            if q.qsize() == 0:
                print("Queue Is Empty, Cannot Delete Element!!!")
            else:
                print("Removed Element:", q.get())
        elif choice == 3:
            length = q.qsize()
            print("Number Of Elements In The Queue:", length)
        elif choice == 4:
            if q.qsize() == 0:
                print("Queue Is Empty")
            else:
                print("Queue Is Not Empty")
        elif choice == 5:
            display_queue(q)
            print("End")
        elif choice == 6:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")
if __name__ == "__main__":
    main()