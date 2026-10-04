import re
import pandas as pd
def preprocess_skills(frame):
    specific_skills = ['c
    all_skills = []
    for _, column in frame.iteritems():
        column = column.replace('>', '').replace('<', '').replace('...', '')
        skills = column.split(',')
        processed_skills = []
        pattern_with_numbers = re.compile(r'([a-z].*[0-9])')
        pattern_with_letters = re.compile(r'([a-z].*[a-z])')
        for skill in skills:
            skill_parts = skill.split(' ')
            if len(skill_parts) <= 4:
                skill = skill.lower().strip()
                if (pattern_with_numbers.match(skill) or
                    pattern_with_letters.match(skill) or
                    skill in specific_skills):
                    cleaned_skill = clean_skill(skill)
                    if cleaned_skill not in processed_skills:
                        processed_skills.append(cleaned_skill)
        all_skills.append(processed_skills)
    return all_skills
def clean_skill(skill):
    replacements = {
        '?': '', '&amp;': '', '.': '', '&': '', '
    }
    for old, new in replacements.items():
        skill = skill.replace(old, new)
    if skill.startswith('.') and not skill.startswith('.net'):
        skill = skill[1:]
    return skill
