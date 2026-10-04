import pandas as pd
import re
from datetime import datetime
from nltk.corpus import stopwords
from wordcloud import WordCloud
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import seaborn as sns
b1 = pd.read_csv('b1.csv')
b1 = b1[(b1['Year'] >= 2011) & (b1['Year'] <= 2019)]
b1['Date'] = b1['Year'].astype(str) + ' ' + b1['Month'] + ' ' + b1['Day'].astype(str)
b1['Date'] = b1['Date'].apply(lambda x: datetime.strptime(x, '%Y %b %d').date())
def fonk1(pattern, b2):
    b2 = b2.lower()
    return 1 if re.search(pattern, b2) else 0
def fonk2(pattern1, pattern2, b2):
    b2 = b2.lower()
    return 1 if re.search(pattern1, b2) and re.search(pattern2, b2) else 0
b1['Article_bank_purdue'] = b1['Article'].apply(lambda x: fonk2('purdue', 'bankruptcy', x))
print("Article_bank_purdue:", b1['Article_bank_purdue'].sum())
for column in ['Header', 'Article']:
    for word in ['opioid', 'purdue', 'bankruptcy']:
        b1[f'{column}_{word}'] = b1[column].apply(lambda x: fonk1(word, x))
        print(f"{column}_{word}:", b1[f'{column}_{word}'].sum())
b1['Date'] = pd.to_datetime(b1['Date'])
b1 = b1.set_index('Date')
b1 = b1['2011-09-26':'2019-09-14']
b1 = b1.drop(['Unnamed: 0'], axis=1)
b3 = b1.groupby(b1.index.year).agg({
    'Article_opioid': 'sum',
    'Article_purdue': 'sum',
    'Article_bank_purdue': 'sum'
})
b4 = b3.corr(method='pearson')
print("Correlation matrix:\n", b4)
sns.set(b5 = {'figure.figsize': (11, 4)})
b6 = b3.plot(marker='o', linestyle='-')
b6.set_ylabel('Number of Articles')
b6.set_title('Number of Articles per Year Containing Certain Words')
b6.legend(b7 = ['Article_opioid', 'Article_purdue', 'Article_bank_purdue'])
plt.savefig('Trend_words.png', b8 = 'tight')
b9 = stopwords.words('english')
b10 = ['one', 'told cnn', 'trump', 'president', 'say', 'said', 'may', 'new', 'according', 'many',
                        'two', 'make', 'made', 'including', 'work', 'need', 'know', 'year', 'still', 'want', 'take',
                        'going', 'state', 'monday', 'first', 'week', 'pr', 'michael', 'jackson', 'donald']
b9.extend(b10)
b11 = np.array(Image.open("usa_map.jpg"))
b12 = WordCloud(background_color="black", max_words=2000, width=800, height=400, b11=b11)
b13 = " ".join(b1[b1['Article_opioid'] == 1]['Article'].apply(
    lambda text: " ".join(word for word in text.lower().split() if word not in b9)))
b12.generate(b13)
b12.to_file("cloud_opioid.png")
b1.to_csv('news_final.csv')