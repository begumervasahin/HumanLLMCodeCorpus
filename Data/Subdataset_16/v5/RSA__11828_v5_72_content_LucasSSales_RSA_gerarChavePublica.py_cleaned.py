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
        self.fonk3("Gerar chave publica", 22, "top")
        self.fonk3("Insira os valores abaixo", 10, "top")
        self.fonk4(5)
        self.fonk5("p:", 80, 65)
        self.fonk5("q:", 80, 90)
        self.fonk5("e:", 80, 115)
        self.fonk6("Gerar chave", self.gerar, 95, 145)
    def fonk3(self, b1, font_size, b12):
        tk.Label(self, b1 = b1, font=('Verdana', font_size)).pack(b12=b12, fill="b3")
    def fonk4(self, count):
        for _ in range(count):
            self.fonk3("", 22, "top")
    def fonk5(self, b1, b3, y):
        b2 = tk.Label(self, b1=b1)
        b2.pack()
        b2.place(b3 = b3, y=y)
        b4 = tk.Entry(self)
        b4.pack()
        b4.place(b3 = b3 + 20, y=y)
        setattr(self, b1[0], b4)
    def fonk6(self, b1, command, b3, y):
        b5 = tk.Button(self, b1=b1, command=command)
        b5.pack()
        b5.place(b3 = b3, y=y)
    def fonk7(self):
        b6 = self.p.get()
        b7 = self.q.get()
        b8 = self.e.get()
        error_message, b9 = pqeValidacao(b6, b7, b8), "ERRO!"
        if not error_message:
            self.fonk8(b6, b7, b8)
            error_message, b9 = "Chave Gerada com Sucesso!", "Concluido"
        tkinter.messagebox.showinfo(b9, error_message)
    def fonk8(self, p, q, e):
        if os.path.exists("chavePublica.txt"):
            os.remove("chavePublica.txt")
        with open("chavePublica.txt", "w") as file:
            file.write(str((int(p) * int(q), int(e))))
if b10 = = "__main__":
    b11 = tk.Tk()
    class1(b11).pack(b12 = "top", fill="both", expand=True)
    b11.mainloop()