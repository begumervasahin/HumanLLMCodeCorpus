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
    b3 = tk.Label(b2, b11="black", fg="white", text="Please rate us on the scale of 5", b7=("Helvetica", 20))
    b3.pack()
    def fonk4(score):
        if score < 4:
            print("Thank you for your feedback. We will improve our system.")
        else:
            print("Thank you for your feedback. We are glad that you liked our system.")
        b2.destroy()
    for score in range(1, 6):
        b4 = tk.Button(b2, text=str(score), b7=("Helvetica", 16), width=50,
                           b5 = lambda s=score: fonk4(s), b11="blue", fg="yellow")
        b4.pack()
    b2.mainloop()
def fonk5():
    b6.destroy()
b6 = tk.Tk()
b6.title('ADA OEP')
b3 = tk.Label(b6, b11="black", fg="white", text="ADA OEP\n\nFloyd Warshall Algorithm\n\nSelect from the following options\n",
                 b7 = ("Helvetica", 20))
b3.pack()
b8 = tk.Button(b6, text='Understand Floyd Warshall Algorithm', b7=("Helvetica", 16), width=50,
                             b5 = open_wikipedia_page, b11="blue", fg="yellow")
b9 = tk.Button(b6, text='Implement Floyd Warshall Algorithm on your b1',
                                  b7 = ("Helvetica", 16), width=50, b5=run_floyd_warshall, b11="blue", fg="yellow")
b10 = tk.Button(b6, text='Feedback', b7=("Helvetica", 16), width=50, b5=open_feedback_window,
                            b11 = "blue", fg="yellow")
b12 = tk.Button(b6, text='Exit', b7=("Helvetica", 16), width=50, b5=exit_program, b11="blue", fg="yellow")
b8.pack()
b9.pack()
b10.pack()
b12.pack()
b6.mainloop()