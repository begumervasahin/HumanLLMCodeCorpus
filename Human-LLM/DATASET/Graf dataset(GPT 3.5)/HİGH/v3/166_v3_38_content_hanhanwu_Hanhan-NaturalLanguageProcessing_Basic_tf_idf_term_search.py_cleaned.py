import nltk
import json
def fonk1(b5):
    with open(b5, 'r') as file:
        return json.load(file)
def fonk2(b6):
    return [activity['object']['content'].lower().split() for activity in b6 if activity['object']['content'] != '']
def fonk3(b8, query_terms):
    b1 = nltk.TextCollection(b8)
    b2 = []
    for i, activity in enumerate(b8):
        b3 = sum(b1.tf_idf(term.lower(), activity) for term in query_terms)
        if b3 > 0:
            b2.append({
                'b3': b3,
                'title': b6[i]['title'],
                'url': b6[i]['url']
            })
    return sorted(b2, b4 = lambda a: a['b3'], reverse=True)
def fonk4(b2):
    for ra in b2:
        print('Title:', ra['title'])
        print('URL:', ra['url'])
        print('Score:', ra['b3'])
        print()
def fonk5():
    b5 = '[change to your googleplus_posts.json location]'
    b6 = fonk1(b5)
    b7 = ['mobile']
    b8 = fonk2(b6)
    b2 = fonk3(b8, b7)
    fonk4(b2)
if b9 = = '__main__':
    fonk5()