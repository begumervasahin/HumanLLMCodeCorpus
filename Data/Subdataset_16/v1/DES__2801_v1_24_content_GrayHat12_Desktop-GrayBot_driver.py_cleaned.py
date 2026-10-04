import GrayAPI
import colorama as clr
def fonk1():
    clr.init(b1 = True)
    b2 = input('Input the Topic to get News On: ')
    b3 = GrayAPI.GrayNews(b2)
    print('MAKE REQUEST:', b3.makeRequest())
    print('REQ ERR:', b3.getRequestError())
    print('SOURCE:', b3.getSource(), b4 = '\n\n')
    b5 = b3.getArticles()
    print('LENGTH:', len(b5), b4 = '\n\n')
    for article in b5:
        print(f"{clr.Fore.RED}TITLE: {clr.Fore.GREEN}{article.getTitle()}")
        print(f"{clr.Fore.RED}AUTHOR: {clr.Fore.GREEN}{article.getAuthor()}")
        print(f"{clr.Fore.RED}URL: {clr.Fore.GREEN}{article.getUrl()}")
        print(f"{clr.Fore.RED}DESCRIPTION: {clr.Fore.GREEN}{article.getShortDesc()}")
        print(f"{clr.Fore.RED}IMAGE: {clr.Fore.GREEN}{article.getImage()}")
        print(f"{clr.Fore.RED}PUBLISHED: {clr.Fore.GREEN}{article.getPublishedAt()}")
        print('\n')
if b6 = = "__main__":
    fonk1()