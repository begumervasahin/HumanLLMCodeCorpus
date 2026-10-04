import GrayAPI
import colorama as clr
def fetch_and_display_news(topic):
    news = GrayAPI.GrayNews(topic)
    print(f'MAKE REQUEST: {news.makeRequest()}')
    print(f'REQ ERR: {news.getRequestError()}')
    print(f'SOURCE: {news.getSource()}\n')
    articles = news.getArticles()
    print(f'LENGTH: {len(articles)}\n')
    for article in articles:
        print_article_details(article)
def print_article_details(article):
    details = [
        ('TITLE', article.getTitle()),
        ('AUTHOR', article.getAuthor()),
        ('URL', article.getUrl()),
        ('DESCRIPTION', article.getShortDesc()),
        ('IMAGE', article.getImage()),
        ('PUBLISHED', article.getPublishedAt())
    ]
    for label, value in details:
        print(f"{clr.Fore.RED}{label}: {clr.Fore.GREEN}{value}")
    print('\n')
def main():
    clr.init(autoreset=True)
    topic = input('Input the Topic to get News On: ')
    fetch_and_display_news(topic)
if __name__ == "__main__":
    main()