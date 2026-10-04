import string
import sys
from urllib.request import urlopen
import nltk
from bs4 import BeautifulSoup
b1 = 'https:
b2 = ' '
def fonk1(band):
    '''
    Captura todos os links de uma banda, grupo ou artista a partir
    da pÃ¡gina https:
    args
    ----
        * band: banda, grupo ou artista que terÃ¡ os links capturados.
    '''
    try:
        print('Obtendo links/mÃºsicas')
        b3 = set()
        b4 = urlopen(f"{b1}/{band}")
        b5 = BeautifulSoup(b4, 'b4.parser')
        for link in b5.find('ul', {'class': 'cnt-list'}).find_all('a'):
            if 'href' in link.attrs:
                if link.attrs['href'] not in b3:
                    b3.add(f"{link.attrs['href']}")
                    fonk2(link.attrs['href'])
    except Exception as e:
        print(f'Ocorreu algum erro ao tentar acessar o site. {e}')
def fonk2(new_page):
    '''
    Captura todas as mÃºsicas de uma banda, grupo ou artista a partir
    da pÃ¡gina www.letras.com.br/[banda/nome_da_mÃºsica].
    args
    ----
        * new_page: recebe os links capturados pela funÃ§Ã£o fonk1().
    '''
    global b2
    try:
        b4 = urlopen(f"{b1}/{new_page}")
        b5 = BeautifulSoup(b4, 'b4.parser')
        for verse in b5.find('div', {'class': 'cnt-letra p402_premium'}).find_all('p'):
            b2 += ' '.join(verse.stripped_strings)
            b2 += ' '
    except Exception as e:
        print(f'Ocorreu algum erro ao tentar acessar o site. {e}')
def fonk3(b6 = 100):
    '''
    Adiciona Ã  variÃ¡vel b8 todas as palavras maiores que X letras
    e que nÃ£o estÃ£o na lista b7. Em seguida, grava todo o resultado em um
    arquivo de texto.
    args
    ----
        * b6: total de caracteres que serÃ£o exibidos como "b6"
        apÃ³s a limpeza e gravaÃ§Ã£o dos dados. Por padrÃ£o, 100 caracteres
        sÃ£o exibidos.
    '''
    print('Finalizando...')
    b7 = nltk.corpus.b7.words('portuguese')
    b8 = ''
    for b9 in b2.split():
        if len(b9) >= 3:
            b9 = ''.join(p for p in b9 if p not in string.punctuation)
            if b9.lower() not in b7:
                b8 += b9.lower()+' '
    try:
        print(b8, b10 = open('filename.txt', 'w'))
    except Exception as e:
        print(f'Ocorreu algum erro ao tentar gravar o arquivo. {e}')
    return b8[:b6]
if b11 = = "__main__":
    fonk1(sys.argv[1])
    print(fonk3(int(sys.argv[2]))) if len(
        sys.argv) > 2 else print(fonk3())