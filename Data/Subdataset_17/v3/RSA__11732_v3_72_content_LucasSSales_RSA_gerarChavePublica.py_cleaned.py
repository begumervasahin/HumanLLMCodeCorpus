import tkinter as tk
import tkinter.messagebox
import os
from sympy.ntheory import isprime
def validate_inputs(p, q, e):
    if not (p.isdigit() and q.isdigit() and e.isdigit()):
        return "Todos os valores devem ser nÃºmeros inteiros."
    p, q, e = int(p), int(q), int(e)
    if not (isprime(p) and isprime(q)):
        return "p e q devem ser nÃºmeros primos."
    if not (1 < e < (p - 1) * (q - 1)):
        return "e deve estar no intervalo (1, (p-1)*(q-1))."
    return ""
class PublicKeyGenerator(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.setup_ui()
    def setup_ui(self):
        self.create_title_label("Gerar chave publica", 22)
        self.create_title_label("Insira os valores abaixo", 10)
        self.add_vertical_space(5)
        self.p_entry = self.create_label_and_entry("p:", 80, 65)
        self.q_entry = self.create_label_and_entry("q:", 80, 90)
        self.e_entry = self.create_label_and_entry("e:", 80, 115)
        self.create_generate_button()
    def create_title_label(self, text, font_size):
        tk.Label(self, text=text, font=('Verdana', font_size)).pack(side="top", fill="x")
    def add_vertical_space(self, count):
        for _ in range(count):
            tk.Label(self, text="", font=('Verdana', 22)).pack(side="top", fill="x")
    def create_label_and_entry(self, text, x, y):
        label = tk.Label(self, text=text)
        label.pack()
        label.place(x=x, y=y)
        entry = tk.Entry(self)
        entry.pack()
        entry.place(x=x+20, y=y)
        return entry
    def create_generate_button(self):
        ok_button = tk.Button(self, text="Gerar chave", command=self.generate_key)
        ok_button.pack()
        ok_button.place(x=95, y=145)
    def generate_key(self):
        p, q, e = self.p_entry.get(), self.q_entry.get(), self.e_entry.get()
        error_message = validate_inputs(p, q, e)
        title = "ERRO!" if error_message else "Concluido"
        if not error_message:
            self.write_public_key(p, q, e)
            error_message = "Chave Gerada com Sucesso!"
        tk.messagebox.showinfo(title, error_message)
    def write_public_key(self, p, q, e):
        if os.path.exists("chavePublica.txt"):
            os.remove("chavePublica.txt")
        with open("chavePublica.txt", "w") as file:
            file.write(str((int(p) * int(q), int(e))))
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x200")
    PublicKeyGenerator(root).pack(side="top", fill="both", expand=True)
    root.mainloop()