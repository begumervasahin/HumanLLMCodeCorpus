from tkinter import *
root = Tk()
root.minsize(380, 600)
root.title("Sorting Algorithms Practice 1")
root.configure(background="turquoise")
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
def create_input_boxes():
    remaining = num_boxes.get()
    if remaining < 5 or remaining > 20:
        label = Label(root, text='You can only sort between 5 and 20 numbers')
        label.grid(row=remaining + 5, column=0, padx=15, pady=1, sticky=N)
    else:
        for i in range(remaining):
            num = IntVar()
            label = Label(root, text=i + 1)
            label.grid(row=i + 6, column=0, padx=10, pady=1, sticky=N)
            entry = Entry(root, textvariable=num)
            entry.grid(row=i + 6, column=1, padx=15, pady=1, sticky=N)
            inputs[i] = num
def sort_numbers():
    values = [inputs[i].get() for i in range(len(inputs))]
    bubble_sort(values)
    sorted_label.config(text='The sorted array is: ' + str(values))
inputs = {}
bubble_button = Button(root, text='Bubble Sort', command=sort_numbers)
bubble_button.grid(row=1, column=0, ipadx=35, padx=40, pady=15, sticky=NW)
merge_button = Button(root, text='Merge Sort', command=sort_numbers)
merge_button.grid(row=1, column=1, ipadx=35, padx=40, pady=15, sticky=NE)
question_label = Label(root, text='How many numbers do you want to sort? (Minimum 5, maximum 20)')
question_label.grid(row=2, padx=180, pady=20, sticky=N)
num_boxes = IntVar()
num_entry = Entry(root, textvariable=num_boxes)
num_entry.grid(row=3, ipadx=30, padx=70, pady=5, sticky=N)
accept_button = Button(root, text='Accept', command=create_input_boxes)
accept_button.grid(row=4, ipadx=30, padx=70, pady=5, sticky=N)
sorted_label = Label(root, text='The sorted array is: ')
sorted_label.grid(row=5, ipadx=30, padx=70, pady=5, sticky=N)
root.mainloop()