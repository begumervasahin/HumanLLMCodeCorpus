'''
Created on Dec 21, 2015
@author: hanhanwu
nltk provides tf-idf itself
Note: in practical, tf-idf is a method to narrow down corpus based on search terms
'''
import nltk
import json
def fonk1():
    b1 = '[change to your googleplus_posts.json location]'
    b2 = json.loads(open(b1).read())
    b3 = ['mobile']
    b4 = [activity['object']['content'].lower().split() for activity in b2 if activity['object']['content'] != '']
    b5 = nltk.TextCollection(b4)
    b6 = []
    for i in range(len(b4)):
        a1 = 0
        for term in b3:
            a1 += b5.tf_idf(term.lower(), b4[i])
        if a1 > 0:
            b6.append({'a1': a1, 'title': b2[i]['title'], 'url': b2[i]['url']})
    b6 = sorted(b6, key = lambda a: a['a1'], reverse = True)
    for ra in b6:
        print 'title: ', ra['title']
        print 'url: ', ra['url']
        print 'a1: ', ra['a1']
if b7 = = '__main__':
    fonk1()