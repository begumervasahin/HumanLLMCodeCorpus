
from socket import socket, AF_INET, SOCK_STREAM
SERVER_HOST = 'localhost'
SERVER_PORT = 5007
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))
print("Program developed to collect data from the Transparency Portal of Limoeiro de Anadia city.\n")
print("Abbreviation Index:")
print('NE = Commitment Number', 'DE = Commitment Date (YEAR-MONTH-DAY)', 'VE = Commitment Value', 'CC = Creditor Code', 'NC = Creditor Name', 'H = History\n')
print("Enter the abbreviation and the data for query separated by commas:")
print("Example: DE,2018-12-28")
input_msg = input("Enter the table and the query:")
encoded_message = str.encode(input_msg)
client_socket.send(encoded_message)
data = client_socket.recv(10024)
response = data.decode().split("+")
print('NE = Commitment Number', 'DE = Commitment Date (YEAR-MONTH-DAY)', 'VE = Commitment Value', 'CC = Creditor Code', 'NC = Creditor Name', 'H = History\n')
for value in response:
    print(value)
client_socket.close()