import tkinter
b1 = []
a1 = 0
def fonk1():
    b2 = int(b6.get())
    a1 = 0
    while (a1 <= b2):
        if (len(b1) < 2):
            b1.append(a1)
        if (len(b1) >= 2):
            b3 = b1[-1] + b1[-2]
            b1.append(b3)
        a1 += 1
    print(b1[-1])
    b9.config(b4 = str(b2)+ "th term is : " + str(b1[-1]))
    b1.clear()
b5 = tkinter.Tk()
b5.title("Fibonacci Sequence")
b6 = tkinter.Entry(b5)
b6.grid(b7 = 0, column = 0, padx = 5, pady= 5)
b6.focus()
b8 = tkinter.Button(b5, b4 = "Find Fibonacci Term Sequence", command = fibSeq)
b8.grid(b7 = 0, column = 1, padx = 5, pady =5 )
b9 = tkinter.Label(b5, b4 = "Result")
b9.grid(b7 = 1, column = 0, sticky = "w", padx = 5, pady = 5)
b5.mainloop()