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
    print(f"{clr.Fore.RED}TITLE: {clr.Fore.GREEN}{article.getTitle()}")
    print(f"{clr.Fore.RED}AUTHOR: {clr.Fore.GREEN}{article.getAuthor()}")
    print(f"{clr.Fore.RED}URL: {clr.Fore.GREEN}{article.getUrl()}")
    print(f"{clr.Fore.RED}DESCRIPTION: {clr.Fore.GREEN}{article.getShortDesc()}")
    print(f"{clr.Fore.RED}IMAGE: {clr.Fore.GREEN}{article.getImage()}")
    print(f"{clr.Fore.RED}PUBLISHED: {clr.Fore.GREEN}{article.getPublishedAt()}")
    print('\n')
def main():
    clr.init(autoreset=True)
    topic = input('Input the Topic to get News On: ')
    fetch_and_display_news(topic)
if __name__ == "__main__":
    main()