import GrayAPI
import colorama as clr
def fonk1(b4):
    b1 = GrayAPI.GrayNews(b4)
    print(f'MAKE REQUEST: {b1.makeRequest()}')
    print(f'REQ ERR: {b1.getRequestError()}')
    print(f'SOURCE: {b1.getSource()}\n')
    b2 = b1.getArticles()
    print(f'LENGTH: {len(b2)}\n')
    for article in b2:
        print(f"{clr.Fore.RED}TITLE: {clr.Fore.GREEN}{article.getTitle()}")
        print(f"{clr.Fore.RED}AUTHOR: {clr.Fore.GREEN}{article.getAuthor()}")
        print(f"{clr.Fore.RED}URL: {clr.Fore.GREEN}{article.getUrl()}")
        print(f"{clr.Fore.RED}DESCRIPTION: {clr.Fore.GREEN}{article.getShortDesc()}")
        print(f"{clr.Fore.RED}IMAGE: {clr.Fore.GREEN}{article.getImage()}")
        print(f"{clr.Fore.RED}PUBLISHED: {clr.Fore.GREEN}{article.getPublishedAt()}")
        print('\n')
def fonk2():
    clr.init(b3 = True)
    b4 = input('Input the Topic to get News On: ')
    fonk1(b4)
if b5 = = "__main__":
    fonk2()