import requests
import pandas as pd
import os, sys
fb_token = ""
try:
    fb_token = os.environ['FB_TOKEN']
except:
    print "Veillez saisir la variable d'environnement FB_TOKEN"
    sys.exit(-1)
fb_pageid = "624258451196"
fb_postid = "12488754962145785"
commentlst = []
datelst = []
url = "https:
while(True):
    posts = requests.get(url)
    posts_json = posts.json()
    for x1 in posts_json['data']:
        commentlst.append(x1.get('message').encode('utf-8').strip())
        datelst.append(x1.get('created_time'))
    next_page = ""
    try:
        next_page = posts_json['paging']['next']
        url = next_page
    except:
        break
    if not next_page: break
    print "Nombre Commantaires: %s,  Page Suivante: %s" % ( len(commentlst), url)
print "\nGeneration de fichier JSON"
df = pd.DataFrame({'commentaire': commentlst, 'dates': datelst})
df['dates'] = pd.to_datetime(df['dates'])
df['day_of_week'] = df['dates'].dt.weekday_name
df['year'] = df['dates'].dt.year
df['month'] = df['dates'].dt.month
df['count'] = 1
df.to_json('commentaires_data.json')