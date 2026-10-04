import pandas as pd
import re
def preprocess_skills(frame):
    specific_skills = ['c
    processed_skills = []
    for skill_string in frame:
        skill_string = skill_string.replace('>', '').replace('<', '').replace('...', '')
        skill_list = skill_string.split(',')
        cleaned_skills = []
        alphanumeric_pattern = re.compile(r'([a-z].*[0-9])')
        alphabetic_pattern = re.compile(r'([a-z].*[a-z])')
        for skill in skill_list:
            skill_parts = skill.split(' ')
            if len(skill_parts) <= 4:
                skill = skill.lower().strip()
                if (alphanumeric_pattern.match(skill) or alphabetic_pattern.match(skill) or skill in specific_skills):
                    skill = skill.replace('?', '').replace('&amp;', '').replace('&', '')
                    skill = skill.replace('
                    if skill.endswith('.'):
                        skill = skill[:-1]
                    if skill.startswith('.') and not skill.startswith('.net'):
                        skill = skill[1:]
                    if skill not in cleaned_skills:
                        cleaned_skills.append(skill.strip())
        processed_skills.append(cleaned_skills)
    return processed_skills
if __name__ == "__main__":
    data = {
        'skills': [
            'Python, Java, C++, HTML, CSS, JavaScript',
            'C
            'Machine Learning, Data Science, AI, Deep Learning'
        ]
    }
    df = pd.DataFrame(data)
    cleaned_skills = preprocess_skills(df['skills'])
    print(cleaned_skills)