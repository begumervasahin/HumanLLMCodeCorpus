import tkinter as tk
import os
import subprocess
from tkinter import simpledialog, messagebox
b1 = tk.Tk()
b1.title("Sentiment Analysis")
b1.geometry("250x150")
b1.resizable(False, False)
def fonk1():
    b2 = simpledialog.askstring("Search Word", "Enter b2 to fetch tweets")
    if b2:
        b2 = "\\" + b2 if b2.startswith('\\') else b2
        subprocess.run(['python', 'tweet.py', b2])
        messagebox.showinfo("Total Fetched Tweets", "Fetched 30 Tweets.\nView them at new_tweets.txt")
        fonk4('new_tweets.txt')
    else:
        messagebox.showwarning("No Keyword", "Please enter a b2.")
def fonk2():
    subprocess.run(['python', 'preprocess.py'])
    b3 = sum(1 for b5 in open('new_preprocessed.txt'))
    messagebox.showinfo("Preprocessing Tweets", f"After preprocessing we have {b3} tweets left. \nView them at new_preprocessed.txt")
    fonk4('new_preprocessed.txt')
def fonk3():
    messagebox.showinfo("CNN model", "Model running....\nThis takes around 5-10mins.\nPlease be patient")
    subprocess.run(['python', 'twitter-b10-cnn.py', '--load', '/home/sujit_surendranath/Music/NLP/twitter-b10-cnn/run20190322-011848', '--custom_input', '"this book sucks"'])
    pos, b4 = 0, 0
    with open('twitter-out.txt', 'r') as f:
        for b5 in f:
            b5 = b5.rstrip()
            if b5 = = 'pos':
                pos += 1
            elif b5 = = "b4":
                b4 += 1
    messagebox.showinfo("Result", f"Positives: {pos}\nNegatives: {b4}")
def fonk4(file_path):
    b6 = tk.Toplevel(b1)
    b6.title("Display Tweets")
    b6.geometry("1000x600")
    b7 = max(len(b5) for b5 in open(file_path))
    b8 = tk.Listbox(b6, height=31, width=b7+5)
    with open(file_path, 'r') as f:
        for i, b5 in enumerate(f, 1):
            b5 = b5.rstrip()
            b8.insert(i, f"{i}: {b5}")
    b8.pack()
def fonk5():
    subprocess.run(['python', 'graph.py'])
def fonk6():
    b9 = {}
    with open('new_tweets.txt', 'r') as tweet, open('twitter-out.txt', 'r') as pree:
        for x, y in zip(tweet, pree):
            b10 = y.rstrip()
            for b11 in x.split(" "):
                b11 = b11.rstrip()
                if b11.startswith('@'):
                    pos_count, b12 = b9.get(b11, [0, 0])
                    if b10 = = 'pos':
                        pos_count += 1
                    elif b10 = = 'b4':
                        b12 += 1
                    b9[b11] = [pos_count, b12]
    b13 = tk.Toplevel(b1)
    b13.title("Count Window")
    b13.geometry("800x600")
    b7 = max(len(b5) for b5 in open('new_tweets.txt'))
    b8 = tk.Listbox(b13, height=21, width=b7+5)
    for i, (tag, value) in enumerate(b9.items(), 1):
        b14 = f"{tag} has Positive Tweets: {value[0]} Negative Tweets: {value[1]}"
        b8.insert(i, b14)
    b8.pack()
    b15 = tk.Button(b13, text='Plot Graph', width=15, command=plot_graph, background='black', foreground="white", highlightthickness=0, bd=0)
    b15.pack()
b16 = tk.Button(b1, text='Fetch Tweets', width=15, command=fetch_tweets, background='white', foreground="black", highlightthickness=0, bd=0)
b16.pack()
b17 = tk.Button(b1, text='Preprocess tweets', width=15, command=preprocess, background='black', foreground="white", highlightthickness=0, bd=0)
b17.pack()
b18 = tk.Button(b1, text='Run Model', width=15, command=run_model, background='white', foreground="black", highlightthickness=0, bd=0)
b18.pack()
b1.mainloop()