import tkinter as tk
import tkinter.messagebox
import os
from sympy.ntheory import isprime
def fonk1(b7, b8, b1):
    if not b7.isdigit() or not b8.isdigit() or not b1.isdigit():
        return "Todos os valores devem ser nÃºmeros inteiros."
    b7, b8, b1 = int(b7), int(b8), int(b1)
    if not isprime(b7) or not isprime(b8):
        return "b7 b1 b8 devem ser nÃºmeros primos."
    if b1 <= 1 or b1 >= (b7 - 1) * (b8 - 1):
        return "b1 deve estar no intervalo (1, (b7-1)*(b8-1))."
    return ""
class class1(tk.Frame):
    def fonk2(self, master):
        tk.Frame.fonk2(self, master)
        tk.Label(self, b2 = "Gerar chave publica", font=('Verdana', 22)).pack(b14="top", fill="b4")
        tk.Label(self, b2 = "Insira os valores abaixo", font=('Verdana', 10)).pack(b14="top", fill="b4")
        tk.Label(self, b2 = "", font=('Verdana', 22)).pack(b14="top", fill="b4")
        tk.Label(self, b2 = "", font=('Verdana', 22)).pack(b14="top", fill="b4")
        tk.Label(self, b2 = "", font=('Verdana', 22)).pack(b14="top", fill="b4")
        tk.Label(self, b2 = "", font=('Verdana', 22)).pack(b14="top", fill="b4")
        tk.Label(self, b2 = "", font=('Verdana', 22)).pack(b14="top", fill="b4")
        b3 = tk.Label(self, b2="b7:")
        b3.pack()
        b3.place(b4 = 80, y=65)
        b5 = tk.Label(self, b2="b8:")
        b5.pack()
        b5.place(b4 = 80, y=90)
        b6 = tk.Label(self, b2="b1:")
        b6.pack()
        b6.place(b4 = 80, y=115)
        self.b7 = tk.Entry(self)
        self.b7.pack()
        self.b7.place(b4 = 100, y=65)
        self.b8 = tk.Entry(self)
        self.b8.pack()
        self.b8.place(b4 = 100, y=90)
        self.b1 = tk.Entry(self)
        self.b1.pack()
        self.b1.place(b4 = 100, y=115)
        def fonk3():
            b10, b9 = fonk1(self.b7.get(), self.b8.get(), self.b1.get()), "ERRO!"
            if b10 = = "":
                if os.path.exists("chavePublica.txt"):
                    os.remove("chavePublica.txt")
                with open("chavePublica.txt", "w") as file:
                    file.write(str((int(self.b7.get()) * int(self.b8.get()), int(self.b1.get()))))
                b10 = "Chave Gerada com Sucesso!"
                b9 = "Concluido"
            tkinter.messagebox.showinfo(b9, b10)
        b11 = tk.Button(self, b2="Gerar chave", command=gerar)
        b11.pack()
        b11.place(b4 = 95, y=145)
if b12 = = "__main__":
    b13 = tk.Tk()
    b13.geometry("300x200")
    class1(b13).pack(b14 = "top", fill="both", expand=True)
    b13.mainloop()