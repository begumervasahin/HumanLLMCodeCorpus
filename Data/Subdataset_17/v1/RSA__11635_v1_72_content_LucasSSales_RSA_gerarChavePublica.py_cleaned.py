import tkinter as tk
import tkinter.messagebox
import os
from sympy.ntheory import isprime
def pqeValidacao(p, q, e):
    if not p.isdigit() or not q.isdigit() or not e.isdigit():
        return "Todos os valores devem ser nÃºmeros inteiros."
    p, q, e = int(p), int(q), int(e)
    if not isprime(p) or not isprime(q):
        return "p e q devem ser nÃºmeros primos."
    if e <= 1 or e >= (p - 1) * (q - 1):
        return "e deve estar no intervalo (1, (p-1)*(q-1))."
    return ""
class Option01(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Gerar chave publica", font=('Verdana', 22)).pack(side="top", fill="x")
        tk.Label(self, text="Insira os valores abaixo", font=('Verdana', 10)).pack(side="top", fill="x")
        tk.Label(self, text="", font=('Verdana', 22)).pack(side="top", fill="x")
        tk.Label(self, text="", font=('Verdana', 22)).pack(side="top", fill="x")
        tk.Label(self, text="", font=('Verdana', 22)).pack(side="top", fill="x")
        tk.Label(self, text="", font=('Verdana', 22)).pack(side="top", fill="x")
        tk.Label(self, text="", font=('Verdana', 22)).pack(side="top", fill="x")
        plb = tk.Label(self, text="p:")
        plb.pack()
        plb.place(x=80, y=65)
        qlb = tk.Label(self, text="q:")
        qlb.pack()
        qlb.place(x=80, y=90)
        elb = tk.Label(self, text="e:")
        elb.pack()
        elb.place(x=80, y=115)
        self.p = tk.Entry(self)
        self.p.pack()
        self.p.place(x=100, y=65)
        self.q = tk.Entry(self)
        self.q.pack()
        self.q.place(x=100, y=90)
        self.e = tk.Entry(self)
        self.e.pack()
        self.e.place(x=100, y=115)
        def gerar():
            err, titulo = pqeValidacao(self.p.get(), self.q.get(), self.e.get()), "ERRO!"
            if err == "":
                if os.path.exists("chavePublica.txt"):
                    os.remove("chavePublica.txt")
                with open("chavePublica.txt", "w") as file:
                    file.write(str((int(self.p.get()) * int(self.q.get()), int(self.e.get()))))
                err = "Chave Gerada com Sucesso!"
                titulo = "Concluido"
            tkinter.messagebox.showinfo(titulo, err)
        okbtn = tk.Button(self, text="Gerar chave", command=gerar)
        okbtn.pack()
        okbtn.place(x=95, y=145)
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x200")
    Option01(root).pack(side="top", fill="both", expand=True)
    root.mainloop()