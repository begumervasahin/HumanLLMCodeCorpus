import pandas as pd
import re
from datetime import datetime
from nltk.corpus import stopwords
from wordcloud import WordCloud
import seaborn as sns
from matplotlib import pyplot as plt
b1 = pd.read_csv('b1.csv')
b1.head()
b1.describe()
b1[['Year']] = b1[['Year']].loc[b1['Year'].apply(lambda x: (x >= 2011) & (x <= 2019))]
b1.shape
list(b1.columns.values)
b1['Date'] = b1['Year'].astype(str) + ' ' + b1['Month'] + ' ' + b1['Day'].astype(str)
b1['Date'] = b1['Date'].apply(lambda x: datetime.strptime(x, '%Y %b %d').date())
def fonk1(pattern, b2):
    b2 = b2.lower()
    if re.search(pattern, b2) != None:
        return 1
    else:
        return 0
def fonk2(pattern1, pattern2, b2):
    b2 = b2.lower()
    if re.search(pattern1, b2) !=None and re.search(pattern2, b2) != None:
        return 1
    else:
        return 0
b3['Article_bank_purdue'] = b3['Article'].apply(lambda x: fonk2('purdue', 'bankruptcy', x))
print(b3['Article_bank_purdue'].sum())
for i in ['Header', 'Article']:
    for y in ['opioid', 'purdue', 'bankruptcy']:
        b1[i + '_' + y] = b1[i].apply(lambda x: fonk2(y, x))
        print(b1[i + '_' + y].sum())
b3['Date'] = pd.to_datetime(b3['Date'])
b3.Date.dtype
b3 = b3.set_index('Date')
b3 = b3['9/26/2011':'9/14/2019']
b3.shape
b3 = b3.drop(['Unnamed: 0'], axis = 1)
b4 = b3.groupby(b3.index.year).agg({'Article_opioid': ['sum'],'Article_purdue': ['sum'],'Article_bank_purdue': ['sum']})
b4
b5 = b3.groupby(b3.index.year).agg({'Article_opioid': ['sum'],'Article_purdue': ['sum'],'Article_bankruptcy': ['sum']})
b6 = b6.corr(method = "pearson")
b6
sns.set(b7 = {'figure.figsize':(11, 4)})
b8 = b3.\
    groupby(b3.index.year).\
    agg({'Article_opioid': ['sum'],'Article_purdue': ['sum'],
         'Article_bank_purdue':['sum']}).\
    plot(b9 = 'o', linestyle = '-')
b8.set_ylabel('Number of Articles')
b8.set_title('Number of Articles per Year Containing Certain Words')
b8.legend(b10 = ['
                    '
plt.savefig('Trend_words.png', b11 = 'tight')
b12 = stopwords.words('english')
b12.extend(['one', 'told cnn', 'trump', 'president', 'say', 'said', 'may', 'new', 'according', 'many', 'two', \
            'make', 'made', 'including', 'work', 'need', 'know', 'year', 'still', 'want', 'take', 'going',\
             'state', 'monday', 'first', 'week', 'pr', 'michael', 'jackson', 'donald'])
b12
b13 = np.array(Image.open("usa_map.jpg"))
b14 = WordCloud(background_color="black", max_words=2000, width=800, height=400, b13 = b13)
b15 = str(b3.loc[b3.Article_opioid == 1]['Article'].\
apply(lambda text: " ".join(word for word in text.lower().split() if word not in b12)))
b14.generate(b15)
b14.to_file("clou_opioid.png")
b3.to_csv('news_final.csv')