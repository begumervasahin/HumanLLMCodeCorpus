import nltk
import json
def fonk1(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
def fonk2(b4):
    return [activity['object']['content'].lower().split() for activity in b4 if activity['object']['content'] != '']
def fonk3(b6, b5, b7):
    b1 = []
    for activity_index, activity_content in enumerate(b6):
        b2 = sum(b7.tf_idf(term.lower(), activity_content) for term in b5)
        if b2 > 0:
            b1.append({
                'b2': b2,
                'title': b4[activity_index]['title'],
                'url': b4[activity_index]['url']
            })
    return b1
def fonk4(b1):
    for activity in b1:
        print('Title:', activity['title'])
        print('URL:', activity['url'])
        print('Score:', activity['b2'])
        print()
def fonk5():
    b3 = '[change to your googleplus_posts.json location]'
    b4 = fonk1(b3)
    b5 = ['mobile']
    b6 = fonk2(b4)
    b7 = nltk.TextCollection(b6)
    b1 = fonk3(b6, b5, b7)
    b1.sort(b8 = lambda activity: activity['b2'], reverse=True)
    fonk4(b1)
if b9 = = '__main__':
    fonk5()