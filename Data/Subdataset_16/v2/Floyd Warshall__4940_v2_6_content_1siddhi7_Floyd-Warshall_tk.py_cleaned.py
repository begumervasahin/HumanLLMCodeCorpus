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
    b3 = tk.Label(b2, bg="black", fg="white", b5="Please rate us on the scale of 5", font=("Helvetica", 20))
    b3.pack()
    def fonk4(rating):
        print(f"Thank you for your feedback\nRating: {rating}")
        b2.destroy()
    b4 = [
        tk.Button(b2, b5 = str(i), font=("Helvetica", 16), width=50,
                  b6 = lambda i=i: fonk4(i), bg="blue", fg="yellow")
        for i in range(1, 6)
    ]
    for b10 in b4:
        b10.pack()
    b2.mainloop()
def fonk5():
    b7.destroy()
def fonk6():
    global b7
    b7 = tk.Tk()
    b7.title('ADA')
    b8 = tk.Label(b7, bg="black", fg="white", b5="ADA OEP\n\nFloyd Warshall Algorithm\n\nSelect from the following options\n", font=("Helvetica", 20))
    b8.pack()
    b9 = [
        ("Understand Floyd Warshall Algorithm", open_wikipedia),
        ("Implement Floyd Warshall Algorithm on your b1", implement_floyd_warshall),
        ("Feedback", feedback),
        ("Exit", exit_application)
    ]
    for b5, b6 in b9:
        b10 = tk.Button(b7, b5=b5, font=("Helvetica", 16), width=50, b6=b6, bg="blue", fg="yellow")
        b10.pack()
    b7.mainloop()
if b11 = = '__main__':
    fonk6()