from socket import *
b1 = 'localhost'
a1 = 5007
b2 = socket(AF_INET,SOCK_STREAM)
b2.connect((b1,a1))
print("Programa desenvolvido para coletar dados do site Portal da TransparÃªncia da cidade de Limoeiro de Anadia.",'\n')
print("indice de AbreciaÃ§Ãµes:")
print('b3 = NÂº do Empenho',' DE = Data do Empenho (ANO-MÃS-DIA)',' VE = Valor do Empenho',' CC = Codigo do Credor',' NC = Nome do Credor',' H = Historico',"\n")
print("Digite a abreviaÃ§Ã£o e o dado para consulta separado por virgulas:")
print("Exemplo: DE,2018-12-28")
b4 = input("Digite a tabela e a consulta:")
b5 = [str.encode(b4)]
for linha in b5:
    b2.send(linha)
    b6 = b2.recv(10024)
    b7 = b6.decode().split("+")
    print('b3 = NÂº do Empenho',' DE = Data do Empenho (ANO-MÃS-DIA)',' VE = Valor do Empenho',' CC = Codigo do Credor',' NC = Nome do Credor',' H = Historico',"\n")
    for valores in b7:
        print(valores)
b2.close