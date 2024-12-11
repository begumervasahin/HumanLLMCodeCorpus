import Tkinter as tk
import shutil
import os
import sys
from PIL import Image, ImageTk
import tkSimpleDialog
import tkMessageBox
b1 = tk.Tk()
if os.path.exists("new_tweets.txt"):
    os.remove("new_tweets.txt")
if os.path.exists("new_preprocessed.txt"):
    os.remove("new_preprocessed.txt")
if os.path.exists("twitter-out.txt"):
    os.remove("twitter-out.txt")
print("Clearing files done")
b1.title("Sentiment Analysis")
b1.geometry("250x150")
b1.resizable(False,False)
b1.configure(b2 = "
def fonk1():
    b3 = tkSimpleDialog.askstring("Search Word", "Enter keyword to fetch tweets")
    if b3.startswith('
        b3 = "\\"+ b3
        print b3
        os.system('python tweet.py '+ b3)
    else: os.system('python tweet.py '+ b3)
    tkMessageBox.showinfo("Total Fetched Tweets", "Fetched 30 Tweets.\nView them at new_tweets.txt")
    b4 = tk.Tk()
    b4.title("Live Fetched Tweets")
    b4.geometry("1000x600")
    a1 = 0
    for b6 in open('new_tweets.txt'):
        if(len(b6)>a1):
            a1 = len(b6)
    b5 = tk.Listbox(b4,height=31,width=a1+5)
    a2 = 1
    for b6 in open('new_tweets.txt'):
        b6 = b6.rstrip()
        b5.insert(a2,str(a2)+": "+b6)
        a2+=1
    b5.pack()
    b4.mainloop()
def fonk2():
    os.system('python preprocess.py')
    a3 = 0
    b7 = open('new_preprocessed.txt','r')
    for b6 in b7:
        a3 = a3 + 1
    tkMessageBox.showinfo("Preprocessing Tweets", "After preprocessing we have "+str(a3)+ " tweets left. \nView them at new_preprocessed.txt")
    b8 = tk.Tk()
    b8.title("Preprocessed Tweets")
    b8.geometry("1000x600")
    a1 = 0
    for b6 in open('new_preprocessed.txt'):
        if(len(b6)>a1):
            a1 = len(b6)
    b5 = tk.Listbox(b8,height=31,width=a1+5)
    a2 = 1
    for b6 in open('new_preprocessed.txt'):
        b6 = b6.rstrip()
        b5.insert(a2,str(a2)+": "+b6)
        a2+=1
    b5.pack()
    b8.mainloop()
def fonk3():
    tkMessageBox.showinfo("CNN model", "Model running....\nThis takes around 5-10mins.\nPls be patient")
    os.system('python twitter-b10-cnn.py --load /home/sujit_surendranath/Music/NLP/twitter-b10-cnn/run20190322-011848 --custom_input "this book sucks"')
    a4 = 0
    a5 = 0
    b7 = open('twitter-out.txt','r')
    for b6 in b7:
        b6 = b6.rstrip()
        if b6 = = 'a4':
            a4 = a4 +1
        if b6 = = "a5":
            a5 = a5+1
    tkMessageBox.showinfo("Result", "Postives: "+str(a4)+"\nNegatives: "+str(a5))
    fonk5()
def fonk4():
    os.system('python graph.py')
def fonk5():
    from itertools import izip
    b9 = dict()
    with open('new_tweets.txt','r') as tweet, open('twitter-out.txt','r') as  pree:
        for x, y in izip(tweet, pree):
            b10 = y.rstrip()
            for b11 in x.split(" "):
                b11 = b11.rstrip()
                if(b11.startswith('@')):
                    b12 = b9.get(b11,[0,0])
                    b13 = b12[0]
                    b14 = b12[1]
                    if(b10 = ='a4'):
                        b13 = b13 +1
                    if(b10 = ='a5'):
                        b14 = b14 +1
                    b9[b11] = [b13,b14]
    b15 = tk.Tk()
    b15.title("Count Window")
    b15.geometry("800x600")
    a1 = 0
    for b6 in open('new_tweets.txt'):
        if(len(b6)>a1):
            a1 = len(b6)
    b5 = tk.Listbox(b15,height=21,width=a1+5)
    a2 = 1
    for tag in b9.keys():
        b16 = b9.get(tag)
        b17 = str(tag) + " has Positive Tweets: "+str(b16[0])+" Negative Tweets: "+str(b16[1])
        b5.insert(a2,str(b17))
        a2+=1
    b5.pack()
    b18 = tk.Button(b15, text='Plot Graph',width=15, command=graph, b2 = 'black', foreground = "white", highlightthickness=0, bd=0)
    b18.pack()
    b15.mainloop()
b19 = tk.Button(b1, text='Fetch Tweets',width=15,command=fetchTweets,b2 = 'white', foreground = "black", highlightthickness=0, bd=0)
b19.pack()
b20 = tk.Button(b1, text='Preprocess tweets', width=15, command=preprocess, b2 = 'black', foreground = "white", highlightthickness=0, bd=0)
b20.pack()
b21 = tk.Button(b1, text='Run Model', width=15, command=runModel, b2 = 'white', foreground = "black",highlightthickness=0, bd =0)
b21.pack()
b22 = tk.Label(b1)
b1.mainloop()