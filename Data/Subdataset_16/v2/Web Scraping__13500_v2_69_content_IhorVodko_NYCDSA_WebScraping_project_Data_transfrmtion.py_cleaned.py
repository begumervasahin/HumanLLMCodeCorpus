import pandas as pd
import re
from datetime import datetime
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from wordcloud import WordCloud
import seaborn as sns
import numpy as np
from PIL import Image
b1 = pd.read_csv('b1.csv')
b1 = b1[(b1['Year'] >= 2011) & (b1['Year'] <= 2019)]
b1['Date'] = b1['Year'].astype(str) + ' ' + b1['Month'] + ' ' + b1['Day'].astype(str)
b1['Date'] = b1['Date'].apply(lambda x: datetime.strptime(x, '%Y %b %d').date())
def fonk1(pattern1, pattern2, b2):
    b2 = b2.lower()
    if re.search(pattern1, b2) is not None and re.search(pattern2, b2) is not None:
        return 1
    else:
        return 0
b1['Article_bank_purdue'] = b1['Article'].apply(lambda x: fonk1('purdue', 'bankruptcy', x))
print(b1['Article_bank_purdue'].sum())
def fonk2(column, keyword):
    return column.apply(lambda x: 1 if re.search(keyword, x.lower()) else 0)
for column in ['Header', 'Article']:
    for keyword in ['opioid', 'purdue', 'bankruptcy']:
        b1[f'{column}_{keyword}'] = fonk2(b1[column], keyword)
        print(b1[f'{column}_{keyword}'].sum())
b1['Date'] = pd.to_datetime(b1['Date'])
b1 = b1.set_index('Date')
b1 = b1['2011-09-26':'2019-09-14']
b1 = b1.drop(columns=['Unnamed: 0'])
b3 = b1.groupby(b1.index.year).agg({
    'Article_opioid': 'sum',
    'Article_purdue': 'sum',
    'Article_bank_purdue': 'sum'
})
print(b3)
b4 = b3.corr(method="pearson")
print(b4)
sns.set(b5 = {'figure.figsize': (11, 4)})
b6 = b3.plot(marker='o', linestyle='-')
b6.set_ylabel('Number of Articles')
b6.set_title('Number of Articles per Year Containing Certain Words')
plt.savefig('Trend_words.png', b7 = 'tight')
b8 = set(stopwords.words('english')).union(set([
    'one', 'told cnn', 'trump', 'president', 'say', 'said', 'may', 'new', 'according', 'many', 'two',
    'make', 'made', 'including', 'work', 'need', 'know', 'year', 'still', 'want', 'take', 'going',
    'state', 'monday', 'first', 'week', 'pr', 'michael', 'jackson', 'donald'
]))
b9 = np.array(Image.open("usa_map.jpg"))
b10 = WordCloud(background_color="black", max_words=2000, width=800, height=400, b9=b9)
b11 = b1.loc[b1.Article_opioid == 1]['Article']
b12 = " ".join(
    word for text in b11
    for word in text.lower().split()
    if word not in b8
)
b10.generate(b12)
b10.to_file("cloud_opioid.png")
b1.to_csv('news_final.csv')