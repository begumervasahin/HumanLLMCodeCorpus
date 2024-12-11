import tkinter as tk
import tkinter.simpledialog as tkSimpleDialog
import tkinter.messagebox as tkMessageBox
import os
from itertools import zip_longest
def fonk1():
    b1 = ["new_tweets.txt", "new_preprocessed.txt", "twitter-out.txt"]
    for file_name in b1:
        if os.path.exists(file_name):
            os.remove(file_name)
    print("Clearing files done")
def fonk2():
    b2 = tkSimpleDialog.askstring("Search Word", "Enter b2 to fetch tweets")
    if b2.startswith(''):
        b2 = "\\" + b2
    os.system('python tweet.py ' + b2)
    tkMessageBox.showinfo("Total Fetched Tweets", "Fetched 30 Tweets.\nView them at new_tweets.txt")
def fonk3():
    os.system('python preprocess.py')
    b3 = sum(1 for b5 in open('new_preprocessed.txt', 'r'))
    tkMessageBox.showinfo("Preprocessing Tweets", f"After preprocessing we have {b3} tweets left.\nView them at new_preprocessed.txt")
def fonk4():
    tkMessageBox.showinfo("CNN model", "Model running....\nThis takes around 5-10mins.\nPlease be patient")
    os.system('python twitter-b7-cnn.py --load /home/sujit_surendranath/Music/NLP/twitter-b7-cnn/run20190322-011848 --custom_input "this book sucks"')
    pos, b4 = 0, 0
    with open('twitter-out.txt', 'r') as f:
        for b5 in f:
            b5 = b5.rstrip()
            if b5 = = 'pos':
                pos += 1
            if b5 = = "b4":
                b4 += 1
    tkMessageBox.showinfo("Result", f"Positives: {pos}\nNegatives: {b4}")
    fonk6()
def fonk5():
    os.system('python graph.py')
def fonk6():
    b6 = {}
    with open('new_tweets.txt', 'r') as tweet, open('twitter-out.txt', 'r') as pree:
        for x, y in zip_longest(tweet, pree):
            b7 = y.rstrip()
            for b8 in x.split(" "):
                b8 = b8.rstrip()
                if b8.startswith('@'):
                    pos_count, b9 = b6.get(b8, [0, 0])
                    if b7 = = 'pos':
                        pos_count += 1
                    if b7 = = 'b4':
                        b9 += 1
                    b6[b8] = [pos_count, b9]
    b10 = tk.Tk()
    b10.title("Count Window")
    b10.geometry("800x600")
    b11 = max(len(b5) for b5 in open('new_tweets.txt', 'r'))
    b12 = tk.Listbox(b10, height=21, width=b11 + 5)
    for tag, counts in b6.items():
        b13 = f"{tag} has Positive Tweets: {counts[0]} Negative Tweets: {counts[1]}"
        b12.insert(tk.END, b13)
    b12.pack()
    b14 = tk.Button(b10, text='Plot Graph', width=15, command=plot_graph, b16='black', foreground="white", highlightthickness=0, bd=0)
    b14.pack()
    b10.mainloop()
b15 = tk.Tk()
b15.title("Sentiment Analysis")
b15.geometry("250x150")
b15.resizable(False, False)
b15.configure(b16 = "")
b17 = tk.Button(b15, text='Fetch Tweets', width=15, command=fetch_tweets, b16='white', foreground="black", highlightthickness=0, bd=0)
b17.pack()
b18 = tk.Button(b15, text='Preprocess tweets', width=15, command=preprocess_tweets, b16='black', foreground="white", highlightthickness=0, bd=0)
b18.pack()
b19 = tk.Button(b15, text='Run Model', width=15, command=run_model, b16='white', foreground="black", highlightthickness=0, bd=0)
b19.pack()
b15.mainloop()