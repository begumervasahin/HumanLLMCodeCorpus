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
    "plaintext": ""
}
def encrypt_plaintext(plaintext):
    DATA_TEMPLATE["plaintext"] = plaintext
    response = requests.post(URL, json=DATA_TEMPLATE, headers=HEADERS, verify=False)
    if response.status_code == 200:
        response_json = response.json()
        return response_json.get("ciphertext")
    else:
        print(f"Request failed with status code {response.status_code}")
        return None
def process_lines(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for count, line in enumerate(infile, start=1):
            plaintext = line.strip().split(',')[0]
            ciphertext = encrypt_plaintext(plaintext)
            if ciphertext:
                print(f"Processed line {count}")
                outfile.write(f"{ciphertext}\n")
            else:
                print(f"No ciphertext found for line {count}")
def main():
    input_file = 'input.txt'
    output_file = 'response.txt'
    process_lines(input_file, output_file)
if __name__ == "__main__":
    main()