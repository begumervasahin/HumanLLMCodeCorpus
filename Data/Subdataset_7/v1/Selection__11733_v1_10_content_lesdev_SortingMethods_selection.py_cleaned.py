import tkinter as tk
import tkinter.simpledialog as simpledialog
def fonk1():
    b1 = int(b12.get())
    b2 = []
    for i in range(0, b1):
        b3 = simpledialog.askinteger("", "Ingresa el numero")
        b2.append(b3)
    b4 = str(b2)
    b15.config(b5 = b4)
    for i in range(0, len(b2)-1):
        b6 = i
        for j in range(i+1, len(b2)):
            if b2[j] < b2[b6]:
                b6 = j
        b7 = b2[b6]
        b2[b6] = b2[i]
        b2[i] = b7
    b8 = str(b2)
    b16.config(b5 = b8)
b9 = tk.Tk()
b9.title("Selection Sort")
b9.configure(b10 = 'SkyBlue2')
b11 = tk.Label(b9, b5="Cuantos numeros vas a ingresar?", font='Helvetica 12', b10='SkyBlue2')
b11.pack()
b1 = tk.IntVar()
b12 = tk.Entry(b9, width=8, textvariable=b1)
b12.pack()
b13 = tk.Button(b9, b5="Ok!", command=select)
b13.pack(b14 = (10, 0))
b15 = tk.Label(b9, b5="", b10='SkyBlue2')
b15.pack(b14 = (10, 0))
b16 = tk.Label(b9, b5="", b10='SkyBlue2')
b16.pack(b14 = (10, 0))
b9.mainloop()