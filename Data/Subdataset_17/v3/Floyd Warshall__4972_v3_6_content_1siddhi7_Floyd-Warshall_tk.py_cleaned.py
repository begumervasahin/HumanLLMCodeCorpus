import tkinter as tk
import webbrowser
import fw
def open_wikipedia():
    webbrowser.open('https:
def implement_floyd_warshall():
    num_vertices, graph = fw.get_graph()
    fw.floyd_warshall(graph, num_vertices)
def feedback():
    feedback_window = tk.Tk()
    feedback_window.title('Feedback')
    feedback_label = tk.Label(
        feedback_window,
        bg="black",
        fg="white",
        text="Please rate us on the scale of 5",
        font=("Helvetica", 20)
    )
    feedback_label.pack()
    def thank_you_message(rating):
        print(f"Thank you for your feedback\nRating: {rating}")
        feedback_window.destroy()
    for i in range(1, 6):
        feedback_button = tk.Button(
            feedback_window,
            text=str(i),
            font=("Helvetica", 16),
            width=50,
            command=lambda i=i: thank_you_message(i),
            bg="blue",
            fg="yellow"
        )
        feedback_button.pack()
    feedback_window.mainloop()
def exit_application():
    root.destroy()
def main():
    global root
    root = tk.Tk()
    root.title('ADA')
    welcome_label = tk.Label(
        root,
        bg="black",
        fg="white",
        text="ADA OEP\n\nFloyd Warshall Algorithm\n\nSelect from the following options\n",
        font=("Helvetica", 20)
    )
    welcome_label.pack()
    buttons = [
        ("Understand Floyd Warshall Algorithm", open_wikipedia),
        ("Implement Floyd Warshall Algorithm on your graph", implement_floyd_warshall),
        ("Feedback", feedback),
        ("Exit", exit_application)
    ]
    for text, command in buttons:
        button = tk.Button(
            root,
            text=text,
            font=("Helvetica", 16),
            width=50,
            command=command,
            bg="blue",
            fg="yellow"
        )
        button.pack()
    root.mainloop()
if __name__ == '__main__':
    main()