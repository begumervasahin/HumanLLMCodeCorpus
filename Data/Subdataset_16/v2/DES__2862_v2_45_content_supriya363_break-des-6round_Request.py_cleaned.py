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
    "b4": ""
}
def fonk1(b9, b10):
    with open(b9, 'r') as infile, open(b10, 'w') as outfile:
        for count, line in enumerate(infile):
            b4 = line.strip().split(',')[0]
            b3["b4"] = b4
            b5 = requests.post(b1, json=b3, headers=b2, verify=False)
            if b5.b6 = = 200:
                b7 = b5.json()
                b8 = b7.get("b8")
                if b8:
                    print(f"Processed line {count + 1}")
                    outfile.write(f"{b8}\n")
                else:
                    print(f"No b8 found in the b5 for line {count + 1}")
            else:
                print(f"Request failed for line {count + 1} with status code {b5.b6}")
def fonk2():
    b9 = 'input.txt'
    b10 = 'b5.txt'
    fonk1(b9, b10)
if b11 = = "__main__":
    fonk2()