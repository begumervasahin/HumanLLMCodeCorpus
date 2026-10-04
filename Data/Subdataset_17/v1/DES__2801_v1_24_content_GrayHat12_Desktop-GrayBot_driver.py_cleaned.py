import GrayAPI
import colorama as clr
def main():
    clr.init(autoreset=True)
    topic = input('Input the Topic to get News On: ')
    news = GrayAPI.GrayNews(topic)
    print('MAKE REQUEST:', news.makeRequest())
    print('REQ ERR:', news.getRequestError())
    print('SOURCE:', news.getSource(), end='\n\n')
    articles = news.getArticles()
    print('LENGTH:', len(articles), end='\n\n')
    for article in articles:
        print(f"{clr.Fore.RED}TITLE: {clr.Fore.GREEN}{article.getTitle()}")
        print(f"{clr.Fore.RED}AUTHOR: {clr.Fore.GREEN}{article.getAuthor()}")
        print(f"{clr.Fore.RED}URL: {clr.Fore.GREEN}{article.getUrl()}")
        print(f"{clr.Fore.RED}DESCRIPTION: {clr.Fore.GREEN}{article.getShortDesc()}")
        print(f"{clr.Fore.RED}IMAGE: {clr.Fore.GREEN}{article.getImage()}")
        print(f"{clr.Fore.RED}PUBLISHED: {clr.Fore.GREEN}{article.getPublishedAt()}")
        print('\n')
if __name__ == "__main__":
    main()