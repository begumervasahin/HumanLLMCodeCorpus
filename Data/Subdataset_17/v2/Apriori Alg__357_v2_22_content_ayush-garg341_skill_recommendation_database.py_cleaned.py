import pandas as pd
def get_skills_from_csv(file_path):
    data = pd.read_csv(file_path)
    skills = data['skills'].apply(lambda x: x.split(',')).tolist()
    return skills
def preprocess_skills(skills):
    cleaned_skills = [[skill.strip().lower() for skill in skill_set] for skill_set in skills]
    return cleaned_skills
from apyori import apriori
def apply_apriori(skills, min_support=0.004, min_confidence=0.5):
    rules = apriori(skills, min_support=min_support, min_confidence=min_confidence)
    return list(rules)
def save_rules_to_csv(rules, file_path):
    with open(file_path, 'w') as file:
        for rule in rules:
            file.write(f"{rule}\n")
import pandas as pd
def recommend_skills(skill, file_path):
    rules = pd.read_csv(file_path, header=None)
    recommendations = []
    for index, row in rules.iterrows():
        if skill in row[0]:
            recommendations.append(row[1])
    return recommendations
from flask import Flask, request, jsonify
from skill_recom import recommend_skills
app = Flask(__name__)
@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    skill = data.get('skill')
    recommendations = recommend_skills(skill, 'apriori_rules.csv')
    return jsonify({'recommendations': recommendations})
if __name__ == "__main__":
    app.run(debug=True)
class DataBase:
    pass
from get_skills import get_skills_from_csv
from preprocess import preprocess_skills
from machine_learning import apply_apriori
from file_handle import save_rules_to_csv
from suggesting_api import app
if __name__ == "__main__":
    skills = get_skills_from_csv('skills.csv')
    cleaned_skills = preprocess_skills(skills)
    rules = apply_apriori(cleaned_skills, min_support=0.004, min_confidence=0.5)
    save_rules_to_csv(rules, 'apriori_rules.csv')
    app.run(debug=True)