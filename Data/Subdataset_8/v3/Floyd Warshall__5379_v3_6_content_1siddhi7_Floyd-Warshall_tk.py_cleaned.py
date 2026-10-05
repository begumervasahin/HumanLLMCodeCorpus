import tkinter as tk
import webbrowser
import fw
def open_wikipedia_page():
    webbrowser.open('https:
def run_floyd_warshall():
    num_vertices, graph = fw.get_graph()
    fw.floydWarshall(graph, num_vertices)
def open_feedback_window():
    feedback_window = tk.Tk()
    feedback_window.title('Feedback')
    label = tk.Label(feedback_window, text="Please rate us on a scale of 1 to 5", font=("Helvetica", 20), bg="black", fg="white")
    label.pack()
    def handle_feedback(score):
        message = "Thank you for your feedback. We will improve our system." if score < 4 else "Thank you for your feedback. We are glad that you liked our system."
        print(message)
        feedback_window.destroy()
    for score in range(1, 6):
        button = tk.Button(feedback_window, text=str(score), font=("Helvetica", 16), width=50,
                           command=lambda s=score: handle_feedback(s), bg="blue", fg="yellow")
        button.pack()
    feedback_window.mainloop()
def exit_program():
    root.destroy()
root = tk.Tk()
root.title('ADA OEP')
label_text = "ADA OEP\n\nFloyd Warshall Algorithm\n\nSelect from the following options\n"
label = tk.Label(root, text=label_text, font=("Helvetica", 20), bg="black", fg="white")
label.pack()
button_wikipedia = tk.Button(root, text='Understand Floyd Warshall Algorithm', font=("Helvetica", 16), width=50,
                             command=open_wikipedia_page, bg="blue", fg="yellow")
button_implementation = tk.Button(root, text='Implement Floyd Warshall Algorithm on your graph',
                                  font=("Helvetica", 16), width=50, command=run_floyd_warshall, bg="blue", fg="yellow")
button_feedback = tk.Button(root, text='Feedback', font=("Helvetica", 16), width=50, command=open_feedback_window,
                            bg="blue", fg="yellow")
button_exit = tk.Button(root, text='Exit', font=("Helvetica", 16), width=50, command=exit_program, bg="blue", fg="yellow")
button_wikipedia.pack()
button_implementation.pack()
button_feedback.pack()
button_exit.pack()
root.mainloop()