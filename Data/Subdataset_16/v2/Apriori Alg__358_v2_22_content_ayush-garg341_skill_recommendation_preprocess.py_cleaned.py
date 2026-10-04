import pandas as pd
import re
def fonk1(frame):
    b1 = ['c
    b2 = []
    for _, b3 in frame.iteritems():
        b3 = b3.replace('>', '')
        b3 = b3.replace('<', '')
        b3 = b3.replace('...', '')
        b4 = b3.split(',')
        b5 = []
        b6 = re.compile(r'([a-z].*[0-9])')
        b7 = re.compile(r'([a-z].*[a-z])')
        for b9 in b4:
            b8 = b9.split(' ')
            if len(b8) <= 4:
                b9 = b9.lower().strip()
                if (b6.match(b9) or b7.match(b9) or b9 in b1):
                    b9 = b9.replace('?', '')
                    b9 = b9.replace('&amp;', '')
                    if b9.endswith('.'):
                        b9 = b9.replace('.', '')
                    b9 = b9.replace('&', '')
                    b9 = b9.replace('
                    if b9.startswith('.') and not b9.startswith('.net'):
                        b9 = b9.replace('.', '')
                    if b9 not in b5:
                        b5.append(b9.strip())
        b2.append(b5)
    return b2
if b10 = = "__main__":
    b11 = {
        'skills': [
            'Python, Java, C++, HTML, CSS, JavaScript',
            'C
            'Machine Learning, Data Science, AI, Deep Learning'
        ]
    }
    b12 = pd.DataFrame(b11)
    b13 = fonk1(b12['skills'])
    print(b13)