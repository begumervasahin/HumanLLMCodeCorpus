
import tkinter as tk
import webbrowser
import fw
if __name__ == '__main__':
    r = tk.Tk()
    w = tk.Label(r,bg="black",fg="white", text="ADA OEP\n\nFloyd Warshall ALgorithm\n\nSelect from the following options\n",font=("Helvetica", 20))
    w.pack()
    def f1():
        webbrowser.open('https:
    def f2():
        n, graph = fw.get_graph()
        fw.floydWarshall(graph, n)
    def f3():
        r1 = tk.Tk()
        w1 = tk.Label(r1,bg="black",fg="white", text="Please rate us on the scale of 5",font=("Helvetica", 20))
        w1.pack()
        def ff1():
            print("thank you for your feedback\nwe will improve our system\n")
            r1.destroy()
        def ff2():
            print("thank you for your feedback\nwe are glad that you liked our system\n")
            r1.destroy()
        r1.title('Feedback')
        feed1 = tk.Button(r1, text='1',font=("Helvetica", 16), width=50,command=ff1,bg="blue",fg="yellow")
        feed2 = tk.Button(r1, text='2',font=("Helvetica", 16), width=50,command=ff1,bg="blue",fg="yellow")
        feed3 = tk.Button(r1, text='3',font=("Helvetica", 16), width=50,command=ff1,bg="blue",fg="yellow")
        feed4 = tk.Button(r1, text='4',font=("Helvetica", 16), width=50,command=ff2,bg="blue",fg="yellow")
        feed5 = tk.Button(r1, text='5',font=("Helvetica", 16), width=50,command=ff2,bg="blue",fg="yellow")
        feed1.pack()
        feed2.pack()
        feed3.pack()
        feed4.pack()
        feed5.pack()
        r1.mainloop()
    def f4():
        r.destroy()
    r.title('ADA')
    b1 = tk.Button(r, text='Understand Floyd Warshall Algorithm',font=("Helvetica", 16), width=50,command=f1,bg="blue",fg="yellow")
    b2 = tk.Button(r, text='Implement Floyd Warshall Algorithm on your graph',font=("Helvetica", 16), width=50,command=f2,bg="blue",fg="yellow")
    b3 = tk.Button(r, text='Feedback',font=("Helvetica", 16), width=50,command=f3,bg="blue",fg="yellow")
    b4 = tk.Button(r, text='Exit',font=("Helvetica", 16), width=50,command=f4,bg="blue",fg="yellow")
    b1.pack()
    b2.pack()
    b3.pack()
    b4.pack()
    r.mainloop()