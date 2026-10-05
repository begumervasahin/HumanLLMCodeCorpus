from socket import *
serverHost = 'localhost'
serverPort = 5007
sock_client_obj = socket(AF_INET,SOCK_STREAM)
sock_client_obj.connect((serverHost,serverPort))
print("Programa desenvolvido para coletar dados do site Portal da TransparÃªncia da cidade de Limoeiro de Anadia.",'\n')
print("indice de AbreciaÃ§Ãµes:")
print('NE = NÂº do Empenho',' DE = Data do Empenho (ANO-MÃS-DIA)',' VE = Valor do Empenho',' CC = Codigo do Credor',' NC = Nome do Credor',' H = Historico',"\n")
print("Digite a abreviaÃ§Ã£o e o dado para consulta separado por virgulas:")
print("Exemplo: DE,2018-12-28")
entrada = input("Digite a tabela e a consulta:")
mensagem = [str.encode(entrada)]
for linha in mensagem:
    sock_client_obj.send(linha)
    data = sock_client_obj.recv(10024)
    resposta = data.decode().split("+")
    print('NE = NÂº do Empenho',' DE = Data do Empenho (ANO-MÃS-DIA)',' VE = Valor do Empenho',' CC = Codigo do Credor',' NC = Nome do Credor',' H = Historico',"\n")
    for valores in resposta:
        print(valores)
sock_client_obj.close