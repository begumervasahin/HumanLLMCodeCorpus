import tkinter as tk
def fonk1():
    b1 = int(b6.get())
    b2 = [0, 1]
    for sNum in range(2, b1 + 1):
        b3 = b2[-1] + b2[-2]
        b2.append(b3)
    if b1 = = 0:
        a1 = 0
    elif b1 = = 1:
        a1 = 1
    else:
        a1 = b2[-1]
    b9.config(b4 = f"{b1}th term is: {a1}")
b5 = tk.Tk()
b5.title("Fibonacci Sequence")
b6 = tk.Entry(b5)
b6.grid(b7 = 0, column=0, padx=5, pady=5)
b6.focus()
b8 = tk.Button(b5, b4="Find Fibonacci Term Sequence", command=fibSeq)
b8.grid(b7 = 0, column=1, padx=5, pady=5)
b9 = tk.Label(b5, b4="Result")
b9.grid(b7 = 1, column=0, sticky="w", padx=5, pady=5)
b5.mainloop()