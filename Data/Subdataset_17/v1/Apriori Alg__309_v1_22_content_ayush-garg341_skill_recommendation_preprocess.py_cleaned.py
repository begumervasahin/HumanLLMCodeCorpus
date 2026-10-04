import pandas as pd
import re
def preprocessing_frame(frame):
    specific_skills = ['c
    big_list = []
    for _, rows in frame.iteritems():
        rows = rows.replace('>', '')
        rows = rows.replace('<', '')
        rows = rows.replace('...', '')
        rows_split = rows.split(',')
        list_skill = []
        pattern1 = re.compile(r'([a-z].*[0-9])')
        pattern2 = re.compile(r'([a-z].*[a-z])')
        for elements in rows_split:
            space_split = elements.split(' ')
            if len(space_split) <= 4:
                elements = elements.lower().strip()
                if (pattern1.match(elements) or pattern2.match(elements) or elements in specific_skills):
                    elements = elements.replace('?', '')
                    elements = elements.replace('&amp;', '')
                    elements = elements.replace('.', '') if elements.endswith('.') else elements
                    elements = elements.replace('&', '')
                    elements = elements.replace('
                    elements = elements.replace('.', '') if elements.startswith('.') and not elements.startswith('.net') else elements
                    if elements not in list_skill:
                        list_skill.append(elements.strip())
        big_list.append(list_skill)
    return big_list
if __name__ == "__main__":
    data = {
        'skills': [
            'Python, Java, C++, HTML, CSS, JavaScript',
            'C
            'Machine Learning, Data Science, AI, Deep Learning'
        ]
    }
    df = pd.DataFrame(data)
    cleaned_skills = preprocessing_frame(df['skills'])
    print(cleaned_skills)