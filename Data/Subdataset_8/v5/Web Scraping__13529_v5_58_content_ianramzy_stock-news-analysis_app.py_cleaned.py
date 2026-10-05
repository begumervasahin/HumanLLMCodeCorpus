from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)
@app.route('/')
def show_form():
    return render_template("input.html")
@app.route('/result', methods=['POST'])
def show_result():
    if request.method == 'POST':
        ticker = request.form.get('Name')
        print("Ticker:", ticker)
        analysis = str(average_sentiment(ticker))
        print("Sentiment Analysis:", analysis)
        links = get_articles(ticker)[:3]
        links = [link[1] for link in links]
        other_half = 100 - int(analysis)
        return render_template("output.html", analysis=analysis, ticker=ticker, links=links, other_half=other_half)
def get_articles(ticker):
    articles = []
    base_url = f"https:
    url = requests.get(base_url)
    soup = BeautifulSoup(url.text, 'html.parser')
    for link in soup.find_all('a'):
        current_link = link.get('href')
        if 'article' in current_link and current_link not in articles:
            articles.append([1, current_link])
    print(f"{len(articles)} articles found")
    return articles
def average_sentiment(ticker):
    articles = get_articles(ticker)
    full_text = ""
    sentiment = 0
    for article in articles:
        full_text += get_article_text(article[1])
        print(f"Downloaded [{len(full_text)} / {len(articles)}]")
    sentiment = calculate_sentiment(full_text)
    return sentiment
def get_article_text(source):
    data = requests.get(source).text
    news_soup = BeautifulSoup(data, 'html.parser')
    paragraphs = [par.text for par in news_soup.find_all('p')]
    paragraphs = paragraphs[2:-6]
    return '\n'.join(paragraphs)
def calculate_sentiment(text):
    documents = {'documents': [{'id': '1', 'text': text}]}
    azure_key = 'd38ac31a3b2c4e0982d3bc540251a162'
    azure_endpoint = 'https:
    sentiment_azure = f'{azure_endpoint}/sentiment'
    headers = {"Ocp-Apim-Subscription-Key": azure_key}
    response = requests.post(sentiment_azure, headers=headers, json=documents)
    sentiments = response.json()
    score = sentiments['documents'][0]['score']
    return int(round(score * 100))
if __name__ == '__main__':
    app.run(debug=True)