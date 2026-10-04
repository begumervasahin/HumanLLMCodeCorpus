import tkinter as tk
import tkinter.messagebox
import os
from sympy.ntheory import isprime
from funcoesAux import pqeValidacao
class class1(tk.Frame):
    def fonk1(self, master):
        super().fonk1(master)
        self.fonk2()
    def fonk2(self):
        tk.Label(self, b1 = "Gerar chave publica", font=('Verdana', 22)).pack(b13="top", fill="b3")
        tk.Label(self, b1 = "Insira os valores abaixo", font=('Verdana', 10)).pack(b13="top", fill="b3")
        for _ in range(5):
            tk.Label(self, b1 = "", font=('Verdana', 22)).pack(b13="top", fill="b3")
        self.fonk3("p:", 80, 65)
        self.fonk3("q:", 80, 90)
        self.fonk3("e:", 80, 115)
        b2 = tk.Button(self, b1="Gerar chave", command=self.gerar)
        b2.pack()
        b2.place(b3 = 95, y=145)
    def fonk3(self, b1, b3, y):
        b4 = tk.Label(self, b1=b1)
        b4.pack()
        b4.place(b3 = b3, y=y)
        b5 = tk.Entry(self)
        b5.pack()
        b5.place(b3 = b3 + 20, y=y)
        setattr(self, b1[0], b5)
    def fonk4(self):
        b6 = self.p.get()
        b7 = self.q.get()
        b8 = self.e.get()
        b10, b9 = pqeValidacao(b6, b7, b8), "ERRO!"
        if b10 = = "":
            self.fonk5(b6, b7, b8)
            b10, b9 = "Chave Gerada com Sucesso!", "Concluido"
        tkinter.messagebox.showinfo(b9, b10)
    def fonk5(self, p, q, e):
        if os.path.exists("chavePublica.txt"):
            os.remove("chavePublica.txt")
        with open("chavePublica.txt", "w") as file:
            file.write(str((int(p) * int(q), int(e))))
if b11 = = "__main__":
    b12 = tk.Tk()
    class1(b12).pack(b13 = "top", fill="both", expand=True)
    b12.mainloop()