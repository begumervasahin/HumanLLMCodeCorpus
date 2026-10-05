
from socket import *
serverHost = 'localhost'
serverPort = 5007
sock_client_obj = socket(AF_INET, SOCK_STREAM)
sock_client_obj.connect((serverHost, serverPort))
print("Program developed to collect data from the Transparency Portal of Limoeiro de Anadia city.", '\n')
print("Abbreviation Index:")
print('NE = Commitment Number', 'DE = Commitment Date (YEAR-MONTH-DAY)', 'VE = Commitment Value', 'CC = Creditor Code', 'NC = Creditor Name', 'H = History', "\n")
print("Enter the abbreviation and the data for query separated by commas:")
print("Example: DE,2018-12-28")
input_msg = input("Enter the table and the query:")
message = [str.encode(input_msg)]
for line in message:
    sock_client_obj.send(line)
    data = sock_client_obj.recv(10024)
    response = data.decode().split("+")
    print('NE = Commitment Number', 'DE = Commitment Date (YEAR-MONTH-DAY)', 'VE = Commitment Value', 'CC = Creditor Code', 'NC = Creditor Name', 'H = History', "\n")
    for values in response:
        print(values)
sock_client_obj.close