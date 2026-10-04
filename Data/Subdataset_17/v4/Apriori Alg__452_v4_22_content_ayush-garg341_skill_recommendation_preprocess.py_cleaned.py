import re
import pandas as pd
def preprocess_skills(frame):
    specific_skills = ['c
    big_list = []
    for _, rows in frame.iteritems():
        rows = rows.replace('>', '').replace('<', '').replace('...', '')
        rows_split = rows.split(',')
        list_skill = []
        pattern1 = re.compile(r'([a-z].*[0-9])')
        pattern2 = re.compile(r'([a-z].*[a-z])')
        for element in rows_split:
            space_split = element.split(' ')
            if len(space_split) <= 4:
                element = element.lower().strip()
                if (pattern1.match(element) or pattern2.match(element) or element in specific_skills):
                    element = clean_skill(element)
                    if element not in list_skill:
                        list_skill.append(element)
        big_list.append(list_skill)
    return big_list
def clean_skill(skill):
    replacements = {
        '?': '', '&amp;': '', '.': '', '&': '', '
    }
    for old, new in replacements.items():
        skill = skill.replace(old, new)
    if skill.startswith('.') and not skill.startswith('.net'):
        skill = skill[1:]
    return skill
