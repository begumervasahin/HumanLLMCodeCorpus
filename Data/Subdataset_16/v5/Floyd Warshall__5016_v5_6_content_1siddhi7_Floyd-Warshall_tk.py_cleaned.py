import tkinter as tk
import webbrowser
import fw
def fonk1():
    webbrowser.open('https:
def fonk2():
    num_vertices, b1 = fw.get_graph()
    fw.floyd_warshall(b1, num_vertices)
def fonk3():
    b2 = tk.Tk()
    b2.title('Feedback')
    b3 = tk.Label(
        b2,
        b4 = "black",
        b5 = "white",
        b6 = "Please rate us on the scale of 5",
        b7 = ("Helvetica", 20)
    )
    b3.pack()
    def fonk4(rating):
        b8 = ("Thank you for your feedback\nWe will improve our system\n"
                   if rating <= 3 else
                   "Thank you for your feedback\nWe are glad that you liked our system\n")
        print(b8)
        b2.destroy()
    for i in range(1, 6):
        b9 = tk.Button(
            b2,
            b6 = str(i),
            b7 = ("Helvetica", 16),
            b10 = 50,
            b11 = lambda i=i: fonk4(i),
            b4 = "blue",
            b5 = "yellow"
        )
        b9.pack()
    b2.mainloop()
def fonk5():
    b12.destroy()
def fonk6():
    global b12
    b12 = tk.Tk()
    b12.title('ADA')
    b13 = tk.Label(
        b12,
        b4 = "black",
        b5 = "white",
        b6 = "ADA OEP\n\nFloyd Warshall Algorithm\n\nSelect from the following options\n",
        b7 = ("Helvetica", 20)
    )
    b13.pack()
    b14 = [
        ("Understand Floyd Warshall Algorithm", open_wikipedia),
        ("Implement Floyd Warshall Algorithm on your b1", implement_floyd_warshall),
        ("Feedback", feedback),
        ("Exit", exit_application)
    ]
    for b6, b11 in b14:
        b15 = tk.Button(
            b12,
            b6 = b6,
            b7 = ("Helvetica", 16),
            b10 = 50,
            b11 = b11,
            b4 = "blue",
            b5 = "yellow"
        )
        b15.pack()
    b12.mainloop()
if b16 = = '__main__':
    fonk6()