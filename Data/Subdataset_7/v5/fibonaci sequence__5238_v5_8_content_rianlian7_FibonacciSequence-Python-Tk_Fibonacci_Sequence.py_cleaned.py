import tkinter as tk
def fonk1():
    try:
        b1 = int(b7.get())
        b2 = fonk2(b1)
        b10.config(b3 = f"{b1}th term is: {b2[-1]}")
    except ValueError:
        b10.config(b3 = "Please enter a valid integer.")
def fonk2(b1):
    b4 = [0, 1]
    while len(b4) <= b1:
        b5 = b4[-1] + b4[-2]
        b4.append(b5)
    return b4
b6 = tk.Tk()
b6.title("Fibonacci Sequence")
b7 = tk.Entry(b6)
b7.grid(b8 = 0, column=0, padx=5, pady=5)
b7.focus()
b9 = tk.Button(b6, b3="Find Fibonacci Term Sequence", command=calculate_fibonacci_sequence)
b9.grid(b8 = 0, column=1, padx=5, pady=5)
b10 = tk.Label(b6, b3="Result")
b10.grid(b8 = 1, column=0, sticky="w", padx=5, pady=5)
b6.mainloop()