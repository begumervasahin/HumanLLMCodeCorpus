import tkinter as tk
def fonk1():
    try:
        b1 = int(b6.get())
        if b1 <= 0:
            b9.config(b2 = "Please enter a positive integer.")
            return
        elif b1 = = 1:
            b9.config(b2 = "1st term is: 0")
            return
        elif b1 = = 2:
            b9.config(b2 = "2nd term is: 1")
            return
        b3 = [0, 1]
        for i in range(2, b1):
            b4 = b3[-1] + b3[-2]
            b3.append(b4)
        b9.config(b2 = f"{b1}th term is: {b3[-1]}")
    except ValueError:
        b9.config(b2 = "Invalid input. Please enter a valid integer.")
b5 = tk.Tk()
b5.title("Fibonacci Sequence")
b6 = tk.Entry(b5)
b6.grid(b7 = 0, column=0, padx=5, pady=5)
b6.focus()
b8 = tk.Button(b5, b2="Find Fibonacci Term Sequence", command=fibonacci_sequence)
b8.grid(b7 = 0, column=1, padx=5, pady=5)
b9 = tk.Label(b5, b2="Result")
b9.grid(b7 = 1, column=0, sticky="w", padx=5, pady=5)
b5.mainloop()