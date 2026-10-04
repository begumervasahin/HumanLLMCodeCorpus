import GrayAPI
import colorama as clr
def fonk1(b5):
    b1 = GrayAPI.GrayNews(b5)
    print(f'MAKE REQUEST: {b1.makeRequest()}')
    print(f'REQ ERR: {b1.getRequestError()}')
    print(f'SOURCE: {b1.getSource()}\n')
    b2 = b1.getArticles()
    print(f'LENGTH: {len(b2)}\n')
    for article in b2:
        fonk2(article)
def fonk2(article):
    b3 = [
        ('TITLE', article.getTitle()),
        ('AUTHOR', article.getAuthor()),
        ('URL', article.getUrl()),
        ('DESCRIPTION', article.getShortDesc()),
        ('IMAGE', article.getImage()),
        ('PUBLISHED', article.getPublishedAt())
    ]
    for label, value in b3:
        print(f"{clr.Fore.RED}{label}: {clr.Fore.GREEN}{value}")
    print('\n')
def fonk3():
    clr.init(b4 = True)
    b5 = input('Input the Topic to get News On: ')
    fonk1(b5)
if b6 = = "__main__":
    fonk3()