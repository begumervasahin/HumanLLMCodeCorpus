import tkinter as tk
import tkinter.simpledialog as tkSimpleDialog
import tkinter.messagebox as tkMessageBox
import os
from itertools import zip_longest
def clear_files():
    files_to_clear = ["new_tweets.txt", "new_preprocessed.txt", "twitter-out.txt"]
    for file_name in files_to_clear:
        if os.path.exists(file_name):
            os.remove(file_name)
    print("Clearing files done")
def fetch_tweets():
    keyword = tkSimpleDialog.askstring("Search Word", "Enter keyword to fetch tweets")
    if keyword.startswith(''):
        keyword = "\\" + keyword
    os.system('python tweet.py ' + keyword)
    tkMessageBox.showinfo("Total Fetched Tweets", "Fetched 30 Tweets.\nView them at new_tweets.txt")
def preprocess_tweets():
    os.system('python preprocess.py')
    count = sum(1 for line in open('new_preprocessed.txt', 'r'))
    tkMessageBox.showinfo("Preprocessing Tweets", f"After preprocessing we have {count} tweets left.\nView them at new_preprocessed.txt")
def run_model():
    tkMessageBox.showinfo("CNN model", "Model running....\nThis takes around 5-10mins.\nPlease be patient")
    os.system('python twitter-sentiment-cnn.py --load /home/sujit_surendranath/Music/NLP/twitter-sentiment-cnn/run20190322-011848 --custom_input "this book sucks"')
    pos, neg = 0, 0
    with open('twitter-out.txt', 'r') as f:
        for line in f:
            line = line.rstrip()
            if line == 'pos':
                pos += 1
            if line == "neg":
                neg += 1
    tkMessageBox.showinfo("Result", f"Positives: {pos}\nNegatives: {neg}")
    display_user_names()
def plot_graph():
    os.system('python graph.py')
def display_user_names():
    counting_positive = {}
    with open('new_tweets.txt', 'r') as tweet, open('twitter-out.txt', 'r') as pree:
        for x, y in zip_longest(tweet, pree):
            sentiment = y.rstrip()
            for word in x.split(" "):
                word = word.rstrip()
                if word.startswith('@'):
                    pos_count, neg_count = counting_positive.get(word, [0, 0])
                    if sentiment == 'pos':
                        pos_count += 1
                    if sentiment == 'neg':
                        neg_count += 1
                    counting_positive[word] = [pos_count, neg_count]
    count_window = tk.Tk()
    count_window.title("Count Window")
    count_window.geometry("800x600")
    max_length = max(len(line) for line in open('new_tweets.txt', 'r'))
    list_box = tk.Listbox(count_window, height=21, width=max_length + 5)
    for tag, counts in counting_positive.items():
        display_string = f"{tag} has Positive Tweets: {counts[0]} Negative Tweets: {counts[1]}"
        list_box.insert(tk.END, display_string)
    list_box.pack()
    button_plot_graph = tk.Button(count_window, text='Plot Graph', width=15, command=plot_graph, background='black', foreground="white", highlightthickness=0, bd=0)
    button_plot_graph.pack()
    count_window.mainloop()
window = tk.Tk()
window.title("Sentiment Analysis")
window.geometry("250x150")
window.resizable(False, False)
window.configure(background="")
button_fetch_tweets = tk.Button(window, text='Fetch Tweets', width=15, command=fetch_tweets, background='white', foreground="black", highlightthickness=0, bd=0)
button_fetch_tweets.pack()
button_preprocess_tweets = tk.Button(window, text='Preprocess tweets', width=15, command=preprocess_tweets, background='black', foreground="white", highlightthickness=0, bd=0)
button_preprocess_tweets.pack()
button_run_model = tk.Button(window, text='Run Model', width=15, command=run_model, background='white', foreground="black", highlightthickness=0, bd=0)
button_run_model.pack()
window.mainloop()