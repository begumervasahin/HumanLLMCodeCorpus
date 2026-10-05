import tkinter as tk
from tkinter import simpledialog, messagebox
import subprocess
def fonk1():
    b1 = simpledialog.askstring("Search Word", "Enter b1 to fetch tweets")
    if b1:
        b1 = "\\" + b1 if b1.startswith('\\') else b1
        subprocess.run(['python', 'tweet.py', b1])
        messagebox.showinfo("Total Fetched Tweets", "Fetched 30 Tweets.\nView them at new_tweets.txt")
        fonk4('new_tweets.txt')
    else:
        messagebox.showwarning("No Keyword", "Please enter a b1.")
def fonk2():
    subprocess.run(['python', 'preprocess.py'])
    b2 = sum(1 for b4 in open('new_preprocessed.txt'))
    messagebox.showinfo("Preprocessing Tweets", f"After preprocessing we have {b2} tweets left. \nView them at new_preprocessed.txt")
    fonk4('new_preprocessed.txt')
def fonk3():
    messagebox.showinfo("CNN model", "Model running....\nThis takes around 5-10mins.\nPlease be patient")
    subprocess.run(['python', 'twitter-sentiment-cnn.py', '--load', '/home/sujit_surendranath/Music/NLP/twitter-sentiment-cnn/run20190322-011848', '--custom_input', '"this book sucks"'])
    pos, b3 = 0, 0
    with open('twitter-out.txt', 'r') as f:
        for b4 in f:
            b4 = b4.rstrip()
            if b4 = = 'pos':
                pos += 1
            elif b4 = = "b3":
                b3 += 1
    messagebox.showinfo("Result", f"Positives: {pos}\nNegatives: {b3}")
def fonk4(file_path):
    b5 = tk.Toplevel(b8)
    b5.title("Display Tweets")
    b5.geometry("1000x600")
    b6 = max(len(b4) for b4 in open(file_path))
    b7 = tk.Listbox(b5, height=31, width=b6+5)
    with open(file_path, 'r') as f:
        for i, b4 in enumerate(f, 1):
            b4 = b4.rstrip()
            b7.insert(i, f"{i}: {b4}")
    b7.pack()
def fonk5():
    subprocess.run(['python', 'graph.py'])
b8 = tk.Tk()
b8.title("Sentiment Analysis")
b8.geometry("250x150")
b8.resizable(False, False)
b9 = tk.Button(b8, text='Fetch Tweets', width=15, command=fetch_tweets, background='white', foreground="black", highlightthickness=0, bd=0)
b9.pack()
b10 = tk.Button(b8, text='Preprocess tweets', width=15, command=preprocess, background='black', foreground="white", highlightthickness=0, bd=0)
b10.pack()
b11 = tk.Button(b8, text='Run Model', width=15, command=run_model, background='white', foreground="black", highlightthickness=0, bd=0)
b11.pack()
b8.mainloop()