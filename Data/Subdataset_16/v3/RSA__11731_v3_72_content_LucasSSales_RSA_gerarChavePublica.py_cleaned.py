import tkinter as tk
import tkinter.messagebox
import os
from sympy.ntheory import isprime
def fonk1(p, q, b1):
    if not (p.isdigit() and q.isdigit() and b1.isdigit()):
        return "Todos os valores devem ser nÃºmeros inteiros."
    p, q, b1 = int(p), int(q), int(b1)
    if not (isprime(p) and isprime(q)):
        return "p b1 q devem ser nÃºmeros primos."
    if not (1 < b1 < (p - 1) * (q - 1)):
        return "b1 deve estar no intervalo (1, (p-1)*(q-1))."
    return ""
class class1(tk.Frame):
    def fonk2(self, master):
        super().fonk2(master)
        self.fonk3()
    def fonk3(self):
        self.fonk4("Gerar chave publica", 22)
        self.fonk4("Insira os valores abaixo", 10)
        self.fonk5(5)
        self.b2 = self.fonk6("p:", 80, 65)
        self.b3 = self.fonk6("q:", 80, 90)
        self.b4 = self.fonk6("b1:", 80, 115)
        self.fonk7()
    def fonk4(self, b5, font_size):
        tk.Label(self, b5 = b5, font=('Verdana', font_size)).pack(b14="top", fill="b7")
    def fonk5(self, count):
        for _ in range(count):
            tk.Label(self, b5 = "", font=('Verdana', 22)).pack(b14="top", fill="b7")
    def fonk6(self, b5, b7, y):
        b6 = tk.Label(self, b5=b5)
        b6.pack()
        b6.place(b7 = b7, y=y)
        b8 = tk.Entry(self)
        b8.pack()
        b8.place(b7 = b7+20, y=y)
        return b8
    def fonk7(self):
        b9 = tk.Button(self, b5="Gerar chave", command=self.generate_key)
        b9.pack()
        b9.place(b7 = 95, y=145)
    def fonk8(self):
        p, q, b1 = self.b2.get(), self.b3.get(), self.b4.get()
        b10 = fonk1(p, q, b1)
        b11 = "ERRO!" if b10 else "Concluido"
        if not b10:
            self.fonk9(p, q, b1)
            b10 = "Chave Gerada com Sucesso!"
        tk.messagebox.showinfo(b11, b10)
    def fonk9(self, p, q, b1):
        if os.path.exists("chavePublica.txt"):
            os.remove("chavePublica.txt")
        with open("chavePublica.txt", "w") as file:
            file.write(str((int(p) * int(q), int(b1))))
if b12 = = "__main__":
    b13 = tk.Tk()
    b13.geometry("300x200")
    class1(b13).pack(b14 = "top", fill="both", expand=True)
    b13.mainloop()