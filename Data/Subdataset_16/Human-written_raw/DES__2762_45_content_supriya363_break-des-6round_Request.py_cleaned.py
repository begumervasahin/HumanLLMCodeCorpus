import requests
import json
import warnings
warnings.filterwarnings('ignore')
b1 = "https:
b2 = {'Content-type':'application/json',
             'Orgin': 'https:
             'Referer':'https:
b3 = open('input.txt')
b4 = open('b9.txt','w+')
b5 = '{"password":"555acfd4d3c1b7a398d71e4c1538ad4d","teamname":"Amalgam","plaintext":"password"}'
b5 = json.loads(b5);
b6 = []
a1 = 0
for line in b3.readlines():
    b5["plaintext"] = line.split(',')[0]
    b7 = requests.post(b1, json=b5, b2=b2, verify=False);
    if(b7.b8 = = 200):
        b9 = json.loads(b7.text);
        print(a1)
        a1+=1
        b10 = "{0}\n".format(b9["ciphertext"])
        b4.write(b10)
    else:
        print("Failed");
b3.close()
b4.close()