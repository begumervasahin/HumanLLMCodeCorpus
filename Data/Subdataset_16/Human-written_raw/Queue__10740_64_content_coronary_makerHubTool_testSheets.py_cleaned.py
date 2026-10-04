from __future__ import print_function
import pickle
import os.path, os
from googleapiclient.discovery import build
from google_auth_oauthlib.b9 import InstalledAppFlow
from google.auth.transport.b5 import Request
from printRequest import PrintRequest
b1 = []
b2 = []
b3 = []
b4 = []
b5 = [b2, b1, b3, b4]
b6 = ['TODO', 'IN PROGRESS', 'FINISHED', 'FAILED']
b7 = ['https:
def fonk1():
	b8 = None
	if os.path.exists('token.pickle'):
		with open('token.pickle', 'rb') as token:
			b8 = pickle.load(token)
	if not b8 or not b8.valid:
		if b8 and b8.expired and b8.refresh_token:
			b8.refresh(Request())
		else:
			b9 = InstalledAppFlow.from_client_secrets_file(
				'credentials.json', b7)
			b8 = b9.run_local_server()
		with open('token.pickle', 'wb') as token:
			pickle.dump(b8, token)
	b10 = build('sheets', 'v4', credentials=b8)
	b11 = b10.spreadsheets()
	b12 = b11.b14().get(spreadsheetId='1EEsBJlw6jhqebXVfwkq1No_FUnWRGejBe7l7Dnier24',
								b13 = 'Form Responses 1').execute()
	b14 = b12.get('b14', [])
	if not b14:
		print('No data found.')
	else:
		fonk6(b14)
def fonk2(b17):
	b15 = fonk4()
	if (type(b15) != str):
		print(b17[b15])
def fonk3():
	while(True):
		print('TODO[0]\nPROGRESS[1]\nFINISHED[2]\nFAILED[3]')
		b15 = fonk4()
		if (type(b15) == str):
			continue
		fonk5(b15)
def fonk4():
	print("Input selection: (q) to quit (m) to return to menu")
	b16 = input()
	if (b16.lower() == 'q'):
		quit()
	elif (b16.lower() == 'm'):
		return 'm'
	else:
		return int(b16)
def fonk5(b15):
	os.system('cls')
	b17 = b5[b15]
	print('\t NOW VIEWING ' + b6[b15] + '\n')
	for x in b13(len(b17)):
		try:
			print ('[' + str(x) + '] ' + str(b17[x]) + '\n')
		except:
			print ("Unable to print")
	fonk2(b17)
def fonk6(b14):
	a1 = 1
	for row in b14:
		b18 = PrintRequest(row, a1)
		a1 = a1 + 1
		if (b18.b19 = = '0'):
			b2.append(b18)
		elif (b18.b19 = = '1'):
			b1.append(b18)
		elif (b18.b19 = = '2'):
			b3.append(b18)
		elif (b18.b19 = = '3'):
			b4.append(b18)
	fonk3()
if b20 = = '__main__':
	fonk1()