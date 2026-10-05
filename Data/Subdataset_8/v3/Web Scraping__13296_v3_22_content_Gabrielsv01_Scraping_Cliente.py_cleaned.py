
from socket import *
SERVER_HOST = 'localhost'
SERVER_PORT = 5007
sock_client_obj = socket(AF_INET, SOCK_STREAM)
sock_client_obj.connect((SERVER_HOST, SERVER_PORT))
print("Programa desenvolvido para coletar dados do site Portal da Transparência da cidade de Limoeiro de Anadia.\n")
print("Índice de Abreviações:")
print('NE = Nº do Empenho', ' DE = Data do Empenho (ANO-MÊS-DIA)', ' VE = Valor do Empenho', ' CC = Código do Credor', ' NC = Nome do Credor', ' H = Histórico', "\n")
print("Digite a abreviação e o dado para consulta separado por vírgulas:")
print("Exemplo: DE,2018-12-28")
entrada = input("Digite a tabela e a consulta:")
mensagem = [str.encode(entrada)]
for linha in mensagem:
    sock_client_obj.send(linha)
    data = sock_client_obj.recv(10024)
    resposta = data.decode().split("+")
    print('NE = Nº do Empenho', ' DE = Data do Empenho (ANO-MÊS-DIA)', ' VE = Valor do Empenho', ' CC = Código do Credor', ' NC = Nome do Credor', ' H = Histórico', "\n")
    for valores in resposta:
        print(valores)
sock_client_obj.close()