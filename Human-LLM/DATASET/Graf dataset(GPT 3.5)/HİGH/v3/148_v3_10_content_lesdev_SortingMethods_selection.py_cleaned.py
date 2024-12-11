import tkinter as tk
import tkinter.simpledialog as simpledialog
def fonk1():
    b1 = int(b12.get())
    b2 = []
    for _ in range(b1):
        b3 = simpledialog.askinteger("", "Ingrese el número")
        b2.append(b3)
    b4 = str(b2)
    b15.config(b5 = b4)
    for i in range(len(b2)-1):
        b6 = i
        for j in range(i+1, len(b2)):
            if b2[j] < b2[b6]:
                b6 = j
        b2[i], b2[b6] = b2[b6], b2[i]
    b7 = str(b2)
    b16.config(b5 = b7)
b8 = tk.Tk()
b8.title("Selection Sort")
b8.configure(b9 = 'SkyBlue2')
b10 = tk.Label(b8, b5="Cuantos numeros vas a ingresar?", font='Helvetica 12', b9='SkyBlue2')
b10.pack()
b11 = tk.IntVar()
b12 = tk.Entry(b8, width=8, textvariable=b11)
b12.pack()
b13 = tk.Button(b8, b5="Ok!", command=perform_selection_sort)
b13.pack(b14 = (10, 0))
b15 = tk.Label(b8, b5="", b9='SkyBlue2')
b15.pack(b14 = (10, 0))
b16 = tk.Label(b8, b5="", b9='SkyBlue2')
b16.pack(b14 = (10, 0))
b8.mainloop()