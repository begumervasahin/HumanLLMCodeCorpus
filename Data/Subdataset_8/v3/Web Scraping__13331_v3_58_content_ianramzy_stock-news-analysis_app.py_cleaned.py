from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)
@app.route('/')
def display_input():
    return render_template("input.html")
@app.route('/result', methods=['POST', 'GET'])
def show_result():
    if request.method == 'POST':
        ticker = request.form.get('Name')
        analysis = str(get_average_sentiment(ticker))
        links = get_article_links(ticker)
        links = [link[1] for link in links[:3]]
        other_half = 100 - int(analysis)
        return render_template("output.html", analysis=analysis, ticker=ticker, links=links, otherHalf=other_half)
def get_article_links(ticker):
    articles = []
    source_url = f"https:
    url = requests.get(source_url)
    data = url.text
    soup = BeautifulSoup(data, 'html.parser')
    for link in soup.find_all('a'):
        current_link = link.get('href')
        if 'article' == current_link[23:30] and current_link not in articles:
            publish_date = str(link.parent.parent.find('small'))[31:41]
            publish_date = publish_date.strip(" ").split("/")
            if publish_date != ['']:
                articles.append([1, current_link])
    print(f"{len(articles)} articles found")
    return articles
def scrape_news_text(source):
    data = requests.get(source).text
    news_soup = BeautifulSoup(data, 'html.parser')
    paragraphs = [par.text for par in news_soup.find_all('p')]
    paragraphs = paragraphs[2:-6]
    news_text = '\n'.join(paragraphs)
    return news_text
def get_average_sentiment(ticker):
    articles = get_article_links(ticker)
    full_text = ""
    sentiment = 0
    for article in articles:
        full_text += replace_text(scrape_news_text(article[1]))
    breaks = len(full_text)
    for i in range(breaks):
        start_idx = i * 5000
        end_idx = (i + 1) * 5000
        sentiment += get_azure_sentiment(full_text[start_idx:end_idx])
    sentiment += get_azure_sentiment(full_text[breaks * 5000:])
    sentiment /= breaks
    sentiment *= 100
    sentiment = int(round(sentiment))
    return sentiment
def get_azure_sentiment(text):
    documents = {'documents': [{'id': '1', 'text': text}]}
    azure_key = 'YOUR_AZURE_KEY'
    azure_endpoint = 'YOUR_AZURE_ENDPOINT'
    sentiment_azure = f"{azure_endpoint}/sentiment"
    headers = {"Ocp-Apim-Subscription-Key": azure_key}
    response = requests.post(sentiment_azure, headers=headers, json=documents)
    sentiments = response.json()
    sentiments = sentiments['documents'][0]['score']
    return sentiments
def replace_text(text):
    bad_list = ["bear", "bearish", "underperform", "underperforming", "sell", "selling", "sold", "decrease",
                "decreasing", "falling", "fall", "fell", "down", "lose", "lost", "losses", "losing", "downturn",
                "short", "shorting", "downside", "risky", "decline", "declining", "fear", "fears", "sell-off"]
    good_list = ["bull", "bullish", "overperform", "overperforming", "buy", "buying", "bought", "increase",
                 "increasing", "rising", "rise", "rised", "up", "gain", "gains", "gained", "profit", "profited","profitable", "profiting", "upturn", "upside"]
    words = text.split(" ")
    words = ["bad" if word in bad_list else word for word in words]
    words = ["good" if word in good_list else word for word in words]
    return " ".join(words)
if __name__ == '__main__':
    app.run(debug=True)