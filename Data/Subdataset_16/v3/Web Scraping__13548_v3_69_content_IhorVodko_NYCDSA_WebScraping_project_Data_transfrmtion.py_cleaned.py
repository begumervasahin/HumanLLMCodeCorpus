import pandas as pd
import re
from datetime import datetime
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from wordcloud import WordCloud
import seaborn as sns
import numpy as np
from PIL import Image
def fonk1(filepath):
    b1 = pd.read_csv(filepath)
    return b1[(b1['Year'] >= 2011) & (b1['Year'] <= 2019)]
def fonk2(b1):
    b1['Date'] = b1['Year'].astype(str) + ' ' + b1['Month'] + ' ' + b1['Day'].astype(str)
    b1['Date'] = b1['Date'].apply(lambda x: datetime.strptime(x, '%Y %b %d').date())
    return b1
def fonk3(pattern1, pattern2, b2):
    b2 = b2.lower()
    return int(re.search(pattern1, b2) is not None and re.search(pattern2, b2) is not None)
def fonk4(b1, b3, keywords):
    for column in b3:
        for keyword in keywords:
            b1[f'{column}_{keyword}'] = b1[column].apply(lambda x: fonk3(keyword, '', x))
            print(f"{column}_{keyword} count: {b1[f'{column}_{keyword}'].sum()}")
    return b1
def fonk5(b1):
    b1['Date'] = pd.to_datetime(b1['Date'])
    b1 = b1.set_index('Date')
    return b1['2011-09-26':'2019-09-14'].drop(b3 = ['Unnamed: 0'])
def fonk6(b1):
    return b1.groupby(b1.index.year).agg({
        'Article_opioid': 'sum',
        'Article_purdue': 'sum',
        'Article_bank_purdue': 'sum'
    })
def fonk7(b13):
    sns.set(b4 = {'figure.figsize': (11, 4)})
    b5 = b13.plot(marker='o', linestyle='-')
    b5.set_ylabel('Number of Articles')
    b5.set_title('Number of Articles per Year Containing Certain Words')
    plt.savefig('Trend_words.png', b6 = 'tight')
def fonk8(b1, mask_image_path, output_path):
    b7 = set(stopwords.words('english')).union(set([
        'one', 'told cnn', 'trump', 'president', 'say', 'said', 'may', 'new', 'according', 'many', 'two',
        'make', 'made', 'including', 'work', 'need', 'know', 'year', 'still', 'want', 'take', 'going',
        'state', 'monday', 'first', 'week', 'pr', 'michael', 'jackson', 'donald'
    ]))
    b8 = np.array(Image.open(mask_image_path))
    b9 = WordCloud(background_color="black", max_words=2000, width=800, height=400, b8=b8)
    b10 = b1.loc[b1.Article_opioid == 1]['Article']
    b11 = " ".join(
        word for text in b10
        for word in text.lower().split()
        if word not in b7
    )
    b9.generate(b11)
    b9.to_file(output_path)
def fonk9():
    b12 = fonk1('b12.csv')
    b12 = fonk2(b12)
    b12['Article_bank_purdue'] = b12['Article'].apply(lambda x: fonk3('purdue', 'bankruptcy', x))
    print(f"Article_bank_purdue count: {b12['Article_bank_purdue'].sum()}")
    b12 = fonk4(b12, ['Header', 'Article'], ['opioid', 'purdue', 'bankruptcy'])
    b12 = fonk5(b12)
    b13 = fonk6(b12)
    print(b13)
    b14 = b13.corr(method="pearson")
    print(b14)
    fonk7(b13)
    fonk8(b12, "usa_map.jpg", "cloud_opioid.png")
    b12.to_csv('news_final.csv')
if b15 = = "__main__":
    fonk9()