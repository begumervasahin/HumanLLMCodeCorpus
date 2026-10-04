import tkinter as tk
def calculate_fibonacci_term():
    try:
        term_number = int(num_entry.get())
        fibonacci_sequence = [0, 1]
        for _ in range(2, term_number + 1):
            next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_term)
        if term_number == 0:
            result = 0
        elif term_number == 1:
            result = 1
        else:
            result = fibonacci_sequence[-1]
        result_label.config(text=f"The {term_number}th term is: {result}")
    except ValueError:
        result_label.config(text="Please enter a valid integer.")
def setup_gui():
    main_window = tk.Tk()
    main_window.title("Fibonacci Sequence Calculator")
    global num_entry
    num_entry = tk.Entry(main_window)
    num_entry.grid(row=0, column=0, padx=5, pady=5)
    num_entry.focus()
    calculate_button = tk.Button(main_window, text="Find Fibonacci Term", command=calculate_fibonacci_term)
    calculate_button.grid(row=0, column=1, padx=5, pady=5)
    global result_label
    result_label = tk.Label(main_window, text="Result")
    result_label.grid(row=1, column=0, columnspan=2, sticky="w", padx=5, pady=5)
    main_window.mainloop()
if __name__ == "__main__":
    setup_gui()