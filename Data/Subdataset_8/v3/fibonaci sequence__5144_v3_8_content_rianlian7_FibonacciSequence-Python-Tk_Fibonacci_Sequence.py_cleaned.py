import tkinter as tk
def fibonacci_sequence():
    try:
        n = int(entry_widget.get())
        if n <= 0:
            result_label.config(text="Please enter a positive integer.")
            return
        elif n == 1:
            result_label.config(text="1st term is: 0")
            return
        elif n == 2:
            result_label.config(text="2nd term is: 1")
            return
        fib_sequence = [0, 1]
        for i in range(2, n):
            next_num = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_num)
        result_label.config(text=f"{n}th term is: {fib_sequence[-1]}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid integer.")
root = tk.Tk()
root.title("Fibonacci Sequence")
entry_widget = tk.Entry(root)
entry_widget.grid(row=0, column=0, padx=5, pady=5)
entry_widget.focus()
button = tk.Button(root, text="Find Fibonacci Term Sequence", command=fibonacci_sequence)
button.grid(row=0, column=1, padx=5, pady=5)
result_label = tk.Label(root, text="Result")
result_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
root.mainloop()