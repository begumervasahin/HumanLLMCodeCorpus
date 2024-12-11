import requests
import pandas as pd
import os
import sys
b1 = ""
try:
    b1 = os.environ['FB_TOKEN']
except KeyError:
    print("Veillez saisir la variable d'environnement FB_TOKEN")
    sys.exit(-1)
b2 = "624258451196"
b3 = "12488754962145785"
b4 = []
b5 = []
b6 = f"https:
while True:
    b7 = requests.get(b6)
    b8 = b7.json()
    for x1 in b8['data']:
        b4.append(x1.get('message').encode('utf-8').strip())
        b5.append(x1.get('created_time'))
    b9 = ""
    try:
        b9 = b8['paging']['next']
        b6 = b9
    except KeyError:
        break
    if not b9:
        break
    print("Nombre Commantaires: %s,  Page Suivante: %s" % (len(b4), b6))
print("\nGeneration de fichier JSON")
b10 = pd.DataFrame({'commentaire': b4, 'dates': b5})
b10['dates'] = pd.to_datetime(b10['dates'])
b10['day_of_week'] = b10['dates'].dt.day_name()
b10['year'] = b10['dates'].dt.year
b10['month'] = b10['dates'].dt.month
b10['count'] = 1
b10.to_json('commentaires_data.json')