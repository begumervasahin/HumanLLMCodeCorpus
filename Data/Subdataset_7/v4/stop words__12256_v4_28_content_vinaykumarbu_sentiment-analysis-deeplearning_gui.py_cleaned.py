import tkinter as tk
import shutil
import os
import sys
from PIL import Image, ImageTk
import tkinter.simpledialog as tkSimpleDialog
import tkinter.messagebox as tkMessageBox
b1 = tk.Tk()
for file_name in ["new_tweets.txt", "new_preprocessed.txt", "twitter-out.txt"]:
    if os.path.exists(file_name):
        os.remove(file_name)
print("Clearing files done")
b1.title("Sentiment Analysis")
b1.geometry("250x150")
b1.resizable(False, False)
b1.configure(b2 = "")
def fonk1():
    b3 = tkSimpleDialog.askstring("Search Word", "Enter b3 to fetch tweets")
    if b3.startswith(''):
        b3 = "\\" + b3
        print(b3)
        os.system('python tweet.py ' + b3)
    else:
        os.system('python tweet.py ' + b3)
    tkMessageBox.showinfo("Total Fetched Tweets", "Fetched 30 Tweets.\nView them at new_tweets.txt")
    b4 = tk.Tk()
    b4.title("Live Fetched Tweets")
    b4.geometry("1000x600")
    a1 = 0
    for b6 in open('new_tweets.txt'):
        if len(b6) > a1:
            a1 = len(b6)
    b5 = tk.Listbox(b4, height=31, width=a1 + 5)
    a2 = 1
    for b6 in open('new_tweets.txt'):
        b6 = b6.rstrip()
        b5.insert(a2, str(a2) + ": " + b6)
        a2 += 1
    b5.pack()
    b4.mainloop()
def fonk2():
    os.system('python preprocess.py')
    a3 = 0
    with open('new_preprocessed.txt', 'r') as f:
        for b6 in f:
            a3 += 1
    tkMessageBox.showinfo("Preprocessing Tweets", "After preprocessing we have " + str(a3) + " tweets left. \nView them at new_preprocessed.txt")
    b7 = tk.Tk()
    b7.title("Preprocessed Tweets")
    b7.geometry("1000x600")
    a1 = 0
    for b6 in open('new_preprocessed.txt'):
        if len(b6) > a1:
            a1 = len(b6)
    b5 = tk.Listbox(b7, height=31, width=a1 + 5)
    a2 = 1
    for b6 in open('new_preprocessed.txt'):
        b6 = b6.rstrip()
        b5.insert(a2, str(a2) + ": " + b6)
        a2 += 1
    b5.pack()
    b7.mainloop()
def fonk3():
    tkMessageBox.showinfo("CNN model", "Model running....\nThis takes around 5-10mins.\nPlease be patient")
    os.system('python twitter-b9-cnn.py --load /home/sujit_surendranath/Music/NLP/twitter-b9-cnn/run20190322-011848 --custom_input "this book sucks"')
    a4 = 0
    a5 = 0
    with open('twitter-out.txt', 'r') as f:
        for b6 in f:
            b6 = b6.rstrip()
            if b6 = = 'a4':
                a4 += 1
            if b6 = = "a5":
                a5 += 1
    tkMessageBox.showinfo("Result", "Positives: " + str(a4) + "\nNegatives: " + str(a5))
    fonk5()
def fonk4():
    os.system('python graph.py')
def fonk5():
    from itertools import zip_longest
    b8 = {}
    with open('new_tweets.txt', 'r') as tweet, open('twitter-out.txt', 'r') as pree:
        for x, y in zip_longest(tweet, pree):
            b9 = y.rstrip()
            for b10 in x.split(" "):
                b10 = b10.rstrip()
                if b10.startswith('@'):
                    b11 = b8.get(b10, [0, 0])
                    b12 = b11[0]
                    b13 = b11[1]
                    if b9 = = 'a4':
                        b12 += 1
                    if b9 = = 'a5':
                        b13 += 1
                    b8[b10] = [b12, b13]
    b14 = tk.Tk()
    b14.title("Count Window")
    b14.geometry("800x600")
    a1 = 0
    for b6 in open('new_tweets.txt'):
        if len(b6) > a1:
            a1 = len(b6)
    b5 = tk.Listbox(b14, height=21, width=a1 + 5)
    a2 = 1
    for tag in b8.keys():
        b15 = b8.get(tag)
        b16 = str(tag) + " has Positive Tweets: " + str(b15[0]) + " Negative Tweets: " + str(b15[1])
        b5.insert(a2, str(b16))
        a2 += 1
    b5.pack()
    b17 = tk.Button(b14, text='Plot Graph', width=15, command=graph, b2='black', foreground="white", highlightthickness=0, bd=0)
    b17.pack()
    b14.mainloop()
b18 = tk.Button(b1, text='Fetch Tweets', width=15, command=fetchTweets, b2='white', foreground="black", highlightthickness=0, bd=0)
b18.pack()
b19 = tk.Button(b1, text='Preprocess tweets', width=15, command=preprocess, b2='black', foreground="white", highlightthickness=0, bd=0)
b19.pack()
b20 = tk.Button(b1, text='Run Model', width=15, command=runModel, b2='white', foreground="black", highlightthickness=0, bd=0)
b20.pack()
b21 = tk.Label(b1)
b1.mainloop()