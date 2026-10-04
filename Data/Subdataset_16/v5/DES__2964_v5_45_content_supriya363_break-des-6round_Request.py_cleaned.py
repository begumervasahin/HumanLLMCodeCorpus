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
    "b8": ""
}
def fonk1(b8):
    b3["b8"] = b8
    b4 = requests.post(b1, json=b3, headers=b2, verify=False)
    if b4.b5 = = 200:
        b6 = b4.json()
        return b6.get("b9")
    else:
        print(f"Request failed with status code {b4.b5}")
        return None
def fonk2(b10, b11):
    with open(b10, 'r') as infile, open(b11, 'w') as outfile:
        for count, line in enumerate(infile, b7 = 1):
            b8 = line.strip().split(',')[0]
            b9 = fonk1(b8)
            if b9:
                print(f"Processed line {count}")
                outfile.write(f"{b9}\n")
            else:
                print(f"No b9 found for line {count}")
def fonk3():
    b10 = 'input.txt'
    b11 = 'b4.txt'
    fonk2(b10, b11)
if b12 = = "__main__":
    fonk3()