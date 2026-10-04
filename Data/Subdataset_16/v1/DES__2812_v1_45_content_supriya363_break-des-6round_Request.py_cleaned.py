import requests
import json
import warnings
warnings.filterwarnings('ignore')
b1 = "https:
b2 = {
    'Content-type': 'application/json',
    'Origin': 'https:
    'Referer': 'https:
}
b3 = {
    "password": "555acfd4d3c1b7a398d71e4c1538ad4d",
    "teamname": "Amalgam",
    "b4": "password"
}
def fonk1(b9, b10):
    with open(b9, 'r') as infile, open(b10, 'w') as outfile:
        for count, line in enumerate(infile.readlines()):
            b4 = line.split(',')[0]
            b3["b4"] = b4
            b5 = requests.post(b1, json=b3, headers=b2, verify=False)
            if b5.b6 = = 200:
                b7 = b5.json()
                b8 = b7.get("b8")
                if b8:
                    print(count)
                    outfile.write(f"{b8}\n")
            else:
                print("Failed")
def fonk2():
    b9 = 'input.txt'
    b10 = 'b5.txt'
    fonk1(b9, b10)
if b11 = = "__main__":
    fonk2()