import tkinter as tk
import webbrowser
import fw
def fonk1():
    webbrowser.open('https:
def fonk2():
    num_vertices, b1 = fw.get_graph()
    fw.floydWarshall(b1, num_vertices)
def fonk3():
    b2 = tk.Tk()
    b2.title('Feedback')
    b3 = tk.Label(b2, text="Please rate us on a scale of 1 to 5", b11=("Helvetica", 20), b13="black", fg="white")
    b3.pack()
    def fonk4(score):
        b4 = "Thank you for your feedback. We will improve our system." if score < 4 else "Thank you for your feedback. We are glad that you liked our system."
        print(b4)
        b2.destroy()
    for score in range(1, 6):
        b5 = tk.Button(b2, text=str(score), b11=("Helvetica", 16), width=50,
                           b6 = lambda s=score: fonk4(s), b13="blue", fg="yellow")
        b5.pack()
    b2.mainloop()
def fonk5():
    b7.destroy()
b7 = tk.Tk()
b7.title('ADA OEP')
b8 = "ADA OEP\n\nFloyd Warshall Algorithm\n\nSelect from the following options\n"
b3 = tk.Label(b7, text=b8, b11=("Helvetica", 20), b13="black", fg="white")
b3.pack()
b9 = tk.Button(b7, text='Understand Floyd Warshall Algorithm', b11=("Helvetica", 16), width=50,
                             b6 = open_wikipedia_page, b13="blue", fg="yellow")
b10 = tk.Button(b7, text='Implement Floyd Warshall Algorithm on your b1',
                                  b11 = ("Helvetica", 16), width=50, b6=run_floyd_warshall, b13="blue", fg="yellow")
b12 = tk.Button(b7, text='Feedback', b11=("Helvetica", 16), width=50, b6=open_feedback_window,
                            b13 = "blue", fg="yellow")
b14 = tk.Button(b7, text='Exit', b11=("Helvetica", 16), width=50, b6=exit_program, b13="blue", fg="yellow")
b9.pack()
b10.pack()
b12.pack()
b14.pack()
b7.mainloop()