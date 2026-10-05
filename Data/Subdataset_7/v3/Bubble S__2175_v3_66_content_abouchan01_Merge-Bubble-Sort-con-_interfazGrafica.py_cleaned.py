from tkinter import *
b1 = Tk()
b1.minsize(380, 600)
b1.title("Sorting Algorithms Practice 1")
b1.configure(b2 = "turquoise")
def fonk1(arr):
    b3 = len(arr)
    for b7 in range(b3):
        for j in range(0, b3-b7-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
def fonk2(arr):
    if len(arr) > 1:
        b4 = len(arr)
        b5 = arr[:b4]
        b6 = arr[b4:]
        fonk2(b5)
        fonk2(b6)
        b7 = j = k = 0
        while b7 < len(b5) and j < len(b6):
            if b5[b7] < b6[j]:
                arr[k] = b5[b7]
                b7 += 1
            else:
                arr[k] = b6[j]
                j += 1
            k += 1
        while b7 < len(b5):
            arr[k] = b5[b7]
            b7 += 1
            k += 1
        while j < len(b6):
            arr[k] = b6[j]
            j += 1
            k += 1
def fonk3():
    b8 = b19.get()
    if b8 < 5 or b8 > 20:
        b9 = Label(b1, b14='You can only sort between 5 and 20 numbers')
        b9.grid(b10 = b8 + 5, column=0, padx=15, pady=1, sticky=N)
    else:
        for b7 in range(b8):
            b11 = IntVar()
            b9 = Label(b1, b14=b7 + 1)
            b9.grid(b10 = b7 + 6, column=0, padx=10, pady=1, sticky=N)
            b12 = Entry(b1, textvariable=b11)
            b12.grid(b10 = b7 + 6, column=1, padx=15, pady=1, sticky=N)
            b15[b7] = b11
def fonk4():
    b13 = [b15[b7].get() for b7 in range(len(b15))]
    fonk1(b13)
    b22.config(b14 = 'The sorted array is: ' + str(b13))
b15 = {}
b16 = Button(b1, b14='Bubble Sort', command=sort_numbers)
b16.grid(b10 = 1, column=0, ipadx=35, padx=40, pady=15, sticky=NW)
b17 = Button(b1, b14='Merge Sort', command=sort_numbers)
b17.grid(b10 = 1, column=1, ipadx=35, padx=40, pady=15, sticky=NE)
b18 = Label(b1, b14='How many numbers do you want to sort? (Minimum 5, maximum 20)')
b18.grid(b10 = 2, padx=180, pady=20, sticky=N)
b19 = IntVar()
b20 = Entry(b1, textvariable=b19)
b20.grid(b10 = 3, ipadx=30, padx=70, pady=5, sticky=N)
b21 = Button(b1, b14='Accept', command=create_input_boxes)
b21.grid(b10 = 4, ipadx=30, padx=70, pady=5, sticky=N)
b22 = Label(b1, b14='The sorted array is: ')
b22.grid(b10 = 5, ipadx=30, padx=70, pady=5, sticky=N)
b1.mainloop()