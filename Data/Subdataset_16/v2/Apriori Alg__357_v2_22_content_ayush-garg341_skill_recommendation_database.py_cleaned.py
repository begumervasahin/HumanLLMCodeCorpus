import pandas as pd
def fonk1(file_path):
    b1 = pd.read_csv(file_path)
    b2 = b1['b2'].apply(lambda x: x.split(',')).tolist()
    return b2
def fonk2(b2):
    b3 = [[b9.strip().lower() for b9 in skill_set] for skill_set in b2]
    return b3
from apyori import apriori
def fonk3(b2, b4 = 0.004, min_confidence=0.5):
    b5 = apriori(b2, b4=b4, min_confidence=min_confidence)
    return list(b5)
def fonk4(b5, file_path):
    with open(file_path, 'w') as file:
        for rule in b5:
            file.write(f"{rule}\n")
import pandas as pd
def fonk5(b9, file_path):
    b5 = pd.read_csv(file_path, header=None)
    b6 = []
    for index, row in b5.iterrows():
        if b9 in row[0]:
            b6.append(row[1])
    return b6
from flask import Flask, request, jsonify
from skill_recom import recommend_skills
b7 = Flask(b10)
@b7.route('/recommend', b8 = ['POST'])
def fonk6():
    b1 = request.get_json()
    b9 = b1.get('b9')
    b6 = fonk5(b9, 'apriori_rules.csv')
    return jsonify({'b6': b6})
if b10 = = "__main__":
    b7.run(b11 = True)
class class1:
    pass
from get_skills import get_skills_from_csv
from preprocess import preprocess_skills
from machine_learning import apply_apriori
from file_handle import save_rules_to_csv
from suggesting_api import b7
if b10 = = "__main__":
    b2 = fonk1('b2.csv')
    b3 = fonk2(b2)
    b5 = fonk3(b3, b4=0.004, min_confidence=0.5)
    fonk4(b5, 'apriori_rules.csv')
    b7.run(b11 = True)