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
        if rating <= 3:
            print("Thank you for your feedback\nWe will improve our system\n")
        else:
            print("Thank you for your feedback\nWe are glad that you liked our system\n")
        b2.destroy()
    for i in range(1, 6):
        b8 = tk.Button(
            b2,
            b6 = str(i),
            b7 = ("Helvetica", 16),
            b9 = 50,
            b10 = lambda i=i: fonk4(i),
            b4 = "blue",
            b5 = "yellow"
        )
        b8.pack()
    b2.mainloop()
def fonk5():
    b11.destroy()
def fonk6():
    global b11
    b11 = tk.Tk()
    b11.title('ADA')
    b12 = tk.Label(
        b11,
        b4 = "black",
        b5 = "white",
        b6 = "ADA OEP\n\nFloyd Warshall Algorithm\n\nSelect from the following options\n",
        b7 = ("Helvetica", 20)
    )
    b12.pack()
    b13 = [
        ("Understand Floyd Warshall Algorithm", open_wikipedia),
        ("Implement Floyd Warshall Algorithm on your b1", implement_floyd_warshall),
        ("Feedback", feedback),
        ("Exit", exit_application)
    ]
    for b6, b10 in b13:
        b14 = tk.Button(
            b11,
            b6 = b6,
            b7 = ("Helvetica", 16),
            b9 = 50,
            b10 = b10,
            b4 = "blue",
            b5 = "yellow"
        )
        b14.pack()
    b11.mainloop()
if b15 = = '__main__':
    fonk6()