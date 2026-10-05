import tkinter as tk
b1 = []
a1 = 0
def fonk1():
    try:
        b2 = int(b6.get())
        a1 = 0
        while a1 <= b2:
            if len(b1) < 2:
                b1.append(a1)
            if len(b1) >= 2:
                b3 = b1[-1] + b1[-2]
                b1.append(b3)
            a1 += 1
        b9.config(b4 = f"{b2}th term is: {b1[-1]}")
        b1.clear()
    except ValueError:
        b9.config(b4 = "Please enter a valid integer.")
b5 = tk.Tk()
b5.title("Fibonacci Sequence")
b6 = tk.Entry(b5)
b6.grid(b7 = 0, column=0, padx=5, pady=5)
b6.focus()
b8 = tk.Button(b5, b4="Find Fibonacci Term Sequence", command=calculate_fibonacci_sequence)
b8.grid(b7 = 0, column=1, padx=5, pady=5)
b9 = tk.Label(b5, b4="Result")
b9.grid(b7 = 1, column=0, sticky="w", padx=5, pady=5)
b5.mainloop()