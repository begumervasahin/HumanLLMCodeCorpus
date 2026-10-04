import requests
import json
import warnings
warnings.filterwarnings('ignore')
URL = "https:
HEADERS = {
    'Content-type': 'application/json',
    'Origin': 'https:
    'Referer': 'https:
}
DATA_TEMPLATE = {
    "password": "555acfd4d3c1b7a398d71e4c1538ad4d",
    "teamname": "Amalgam",
    "plaintext": "password"
}
def process_lines(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for count, line in enumerate(infile.readlines()):
            plaintext = line.split(',')[0]
            DATA_TEMPLATE["plaintext"] = plaintext
            response = requests.post(URL, json=DATA_TEMPLATE, headers=HEADERS, verify=False)
            if response.status_code == 200:
                response_json = response.json()
                ciphertext = response_json.get("ciphertext")
                if ciphertext:
                    print(count)
                    outfile.write(f"{ciphertext}\n")
            else:
                print("Failed")
def main():
    input_file = 'input.txt'
    output_file = 'response.txt'
    process_lines(input_file, output_file)
if __name__ == "__main__":
    main()