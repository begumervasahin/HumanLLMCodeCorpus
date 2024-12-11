
from socket import *
b1 = 'localhost'
a1 = 5007
b2 = socket(AF_INET, SOCK_STREAM)
b2.connect((b1, a1))
print("Program developed to collect b6 from the Transparency Portal of Limoeiro de Anadia city.", '\n')
print("Abbreviation Index:")
print('b3 = Commitment Number', 'DE = Commitment Date (YEAR-MONTH-DAY)', 'VE = Commitment Value', 'CC = Creditor Code', 'NC = Creditor Name', 'H = History', "\n")
print("Enter the abbreviation and the b6 for query separated by commas:")
print("Example: DE,2018-12-28")
b4 = input("Enter the table and the query:")
b5 = [str.encode(b4)]
for line in b5:
    b2.send(line)
    b6 = b2.recv(10024)
    b7 = b6.decode().split("+")
    print('b3 = Commitment Number', 'DE = Commitment Date (YEAR-MONTH-DAY)', 'VE = Commitment Value', 'CC = Creditor Code', 'NC = Creditor Name', 'H = History', "\n")
    for values in b7:
        print(values)
b2.close