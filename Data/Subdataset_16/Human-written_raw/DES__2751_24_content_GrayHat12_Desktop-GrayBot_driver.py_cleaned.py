import GrayAPI
import colorama as clr
b1 = input('Input the Topic to get News On : ')
b2 = GrayAPI.GrayNews(b1)
print('MAKE REQUEST ', b2.makeRequest())
print('REQ ERR ', b2.getRequestError())
print('SOURCE ', b2.getSource(),b3 = '\n\n')
b4 = b2.getArticles()
print('LENGTH : ', len(b4),b3 = '\n\n')
clr.init(b5 = True)
for ar in b4:
    print(clr.Fore.RED+'TITLE : ', clr.Fore.GREEN+str(ar.getTitle()))
    print(clr.Fore.RED+'AUTHOR : ', clr.Fore.GREEN+str(ar.getAuthor()))
    print(clr.Fore.RED+'URL : ', clr.Fore.GREEN+str(ar.getUrl()))
    print(clr.Fore.RED+'DESCRIPTION : ', clr.Fore.GREEN+str(ar.getShortDesc()))
    print(clr.Fore.RED+'IMAGE : ', clr.Fore.GREEN+str(ar.getImage()))
    print(clr.Fore.RED+'PUBLISHED : ', clr.Fore.GREEN+str(ar.getPublishedAt()))
    print('\n\n')