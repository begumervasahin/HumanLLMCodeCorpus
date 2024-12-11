
import tkinter as tk
import webbrowser
import fw
if b12 = = '__main__':
    b13 = tk.Tk()
    b14 = tk.Label(b13,bg="black",fg="white", text="ADA OEP\n\nFloyd Warshall ALgorithm\n\nSelect from the following options\n",font=("Helvetica", 20))
    b14.pack()
    def fonk1():
        webbrowser.open('https:
    def fonk2():
        n, b15 = fw.get_graph()
        fw.floydWarshall(b15, n)
    def fonk3():
        b5 = tk.Tk()
        b6 = tk.Label(b5,bg="black",fg="white", text="Please rate us on the scale of 5",font=("Helvetica", 20))
        b6.pack()
        def fonk4():
            print("thank you for your feedback\nwe will improve our system\n")
            b5.destroy()
        def fonk5():
            print("thank you for your feedback\nwe are glad that you liked our system\n")
            b5.destroy()
        b5.title('Feedback')
        b7 = tk.Button(b5, text='1',font=("Helvetica", 16), width=50,command=ff1,bg="blue",fg="yellow")
        b8 = tk.Button(b5, text='2',font=("Helvetica", 16), width=50,command=ff1,bg="blue",fg="yellow")
        b9 = tk.Button(b5, text='3',font=("Helvetica", 16), width=50,command=ff1,bg="blue",fg="yellow")
        b10 = tk.Button(b5, text='4',font=("Helvetica", 16), width=50,command=ff2,bg="blue",fg="yellow")
        b11 = tk.Button(b5, text='5',font=("Helvetica", 16), width=50,command=ff2,bg="blue",fg="yellow")
        b7.pack()
        b8.pack()
        b9.pack()
        b10.pack()
        b11.pack()
        b5.mainloop()
    def fonk6():
        b13.destroy()
    b13.title('ADA')
    b12 = tk.Button(b13, text='Understand Floyd Warshall Algorithm',font=("Helvetica", 16), width=50,command=f1,bg="blue",fg="yellow")
    b13 = tk.Button(b13, text='Implement Floyd Warshall Algorithm on your b15',font=("Helvetica", 16), width=50,command=f2,bg="blue",fg="yellow")
    b14 = tk.Button(b13, text='Feedback',font=("Helvetica", 16), width=50,command=f3,bg="blue",fg="yellow")
    b15 = tk.Button(b13, text='Exit',font=("Helvetica", 16), width=50,command=f4,bg="blue",fg="yellow")
    b12.pack()
    b13.pack()
    b14.pack()
    b15.pack()
    b13.mainloop()