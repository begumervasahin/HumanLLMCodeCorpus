import tkinter as tk
def fonk1():
    try:
        b1 = int(b6.get())
        if b1 < 0:
            b9.config(b2 = "Please enter a non-negative integer.")
            return
        b3 = [0, 1]
        for _ in range(2, b1 + 1):
            b4 = b3[-1] + b3[-2]
            b3.append(b4)
        if b1 = = 0:
            a1 = 0
        elif b1 = = 1:
            a1 = 1
        else:
            a1 = b3[-1]
        b9.config(b2 = f"The {b1}th term is: {a1}")
    except ValueError:
        b9.config(b2 = "Please enter a valid integer.")
def fonk2():
    b5 = tk.Tk()
    b5.title("Fibonacci Sequence Calculator")
    tk.Label(b5, b2 = "Enter term number:").grid(b7=0, column=0, padx=5, pady=5)
    global b6
    b6 = tk.Entry(b5)
    b6.grid(b7 = 0, column=1, padx=5, pady=5)
    b6.focus()
    b8 = tk.Button(b5, b2="Find Fibonacci Term", command=calculate_fibonacci_term)
    b8.grid(b7 = 1, column=0, columnspan=2, padx=5, pady=5)
    global b9
    b9 = tk.Label(b5, b2="Result")
    b9.grid(b7 = 2, column=0, columnspan=2, sticky="w", padx=5, pady=5)
    b5.mainloop()
if b10 = = "__main__":
    fonk2()