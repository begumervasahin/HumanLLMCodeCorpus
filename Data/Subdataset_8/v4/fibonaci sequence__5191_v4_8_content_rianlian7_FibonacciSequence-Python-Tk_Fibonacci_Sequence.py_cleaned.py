import tkinter as tk
sequence = []
current_num = 0
def calculate_fibonacci_sequence():
    try:
        num = int(entry.get())
        current_num = 0
        while current_num <= num:
            if len(sequence) < 2:
                sequence.append(current_num)
            if len(sequence) >= 2:
                next_num = sequence[-1] + sequence[-2]
                sequence.append(next_num)
            current_num += 1
        result_label.config(text=f"{num}th term is: {sequence[-1]}")
        sequence.clear()
    except ValueError:
        result_label.config(text="Please enter a valid integer.")
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