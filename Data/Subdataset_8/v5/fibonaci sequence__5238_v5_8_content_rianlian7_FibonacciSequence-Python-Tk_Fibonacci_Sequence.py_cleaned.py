import tkinter as tk
def calculate_fibonacci_sequence():
    try:
        num = int(entry.get())
        fib_sequence = generate_fibonacci_sequence(num)
        result_label.config(text=f"{num}th term is: {fib_sequence[-1]}")
    except ValueError:
        result_label.config(text="Please enter a valid integer.")
def generate_fibonacci_sequence(num):
    sequence = [0, 1]
    while len(sequence) <= num:
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence
root = tk.Tk()
root.title("Fibonacci Sequence")
entry = tk.Entry(root)
entry.grid(row=0, column=0, padx=5, pady=5)
entry.focus()
button = tk.Button(root, text="Find Fibonacci Term Sequence", command=calculate_fibonacci_sequence)
button.grid(row=0, column=1, padx=5, pady=5)
result_label = tk.Label(root, text="Result")
result_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
root.mainloop()