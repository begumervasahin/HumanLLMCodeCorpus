import pandas as pd
import re
from datetime import datetime
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from wordcloud import WordCloud
import seaborn as sns
import numpy as np
from PIL import Image
def load_and_filter_data(filepath):
    data = pd.read_csv(filepath)
    return data[(data['Year'] >= 2011) & (data['Year'] <= 2019)]
def combine_date_columns(data):
    data['Date'] = data['Year'].astype(str) + ' ' + data['Month'] + ' ' + data['Day'].astype(str)
    data['Date'] = data['Date'].apply(lambda x: datetime.strptime(x, '%Y %b %d').date())
    return data
def check_keywords(pattern1, pattern2, string):
    string = string.lower()
    return int(re.search(pattern1, string) is not None and re.search(pattern2, string) is not None)
def create_keyword_columns(data, columns, keywords):
    for column in columns:
        for keyword in keywords:
            data[f'{column}_{keyword}'] = data[column].apply(lambda x: check_keywords(keyword, '', x))
            print(f"{column}_{keyword} count: {data[f'{column}_{keyword}'].sum()}")
    return data
def preprocess_data(data):
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.set_index('Date')
    return data['2011-09-26':'2019-09-14'].drop(columns=['Unnamed: 0'])
def group_and_aggregate(data):
    return data.groupby(data.index.year).agg({
        'Article_opioid': 'sum',
        'Article_purdue': 'sum',
        'Article_bank_purdue': 'sum'
    })
def plot_trend(df_grouped):
    sns.set(rc={'figure.figsize': (11, 4)})
    ax = df_grouped.plot(marker='o', linestyle='-')
    ax.set_ylabel('Number of Articles')
    ax.set_title('Number of Articles per Year Containing Certain Words')
    plt.savefig('Trend_words.png', bbox_inches='tight')
def create_wordcloud(data, mask_image_path, output_path):
    stop_words = set(stopwords.words('english')).union(set([
        'one', 'told cnn', 'trump', 'president', 'say', 'said', 'may', 'new', 'according', 'many', 'two',
        'make', 'made', 'including', 'work', 'need', 'know', 'year', 'still', 'want', 'take', 'going',
        'state', 'monday', 'first', 'week', 'pr', 'michael', 'jackson', 'donald'
    ]))
    mask = np.array(Image.open(mask_image_path))
    wc = WordCloud(background_color="black", max_words=2000, width=800, height=400, mask=mask)
    articles_with_opioid = data.loc[data.Article_opioid == 1]['Article']
    for_cloud = " ".join(
        word for text in articles_with_opioid
        for word in text.lower().split()
        if word not in stop_words
    )
    wc.generate(for_cloud)
    wc.to_file(output_path)
def main():
    news = load_and_filter_data('news.csv')
    news = combine_date_columns(news)
    news['Article_bank_purdue'] = news['Article'].apply(lambda x: check_keywords('purdue', 'bankruptcy', x))
    print(f"Article_bank_purdue count: {news['Article_bank_purdue'].sum()}")
    news = create_keyword_columns(news, ['Header', 'Article'], ['opioid', 'purdue', 'bankruptcy'])
    news = preprocess_data(news)
    df_grouped = group_and_aggregate(news)
    print(df_grouped)
    df_corr = df_grouped.corr(method="pearson")
    print(df_corr)
    plot_trend(df_grouped)
    create_wordcloud(news, "usa_map.jpg", "cloud_opioid.png")
    news.to_csv('news_final.csv')
if __name__ == "__main__":
    main()