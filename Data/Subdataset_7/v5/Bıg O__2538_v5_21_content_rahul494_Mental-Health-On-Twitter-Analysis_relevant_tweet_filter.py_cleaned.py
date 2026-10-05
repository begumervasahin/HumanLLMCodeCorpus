import sys
import csv
import time
b1 = [
    'abuse', 'eatingdisorders', 'nostigma', 'presspause', 'addiction', 'endthestigma', 'nostigmas',
    'mentalhealthmatters', 'alzheimers', 'IAmStigmaFree', '1SmallAct', 'ocd', 'anxiety', 'mentalhealth',
    'psychology', 'suicideprevention', 'bipolar', 'pts', 'mhchat', 'therapy', 'bpd', 'anxiety', 'schizophrenia',
    'trauma', 'Operationalstress', 'therapy', 'ptsd', 'mhsm', 'endthestigma', 'psychology', 'worldmentalhealthday',
    'trauma', 'AA', 'schizophrenia', 'stress', 'spsm', 'mentalhealthmatters', 'stigma', 'wellbeing', 'alcoholism',
    'mentalhealthawareness', 'stopsuicide', 'adhd', 'depressed', 'mentalillness', 'suicide', 'bpd', 'depression', 'MH',
    'shellshock', 'bts'
]
with open('filtered_tweets_per_abused_user.csv', 'w', b2 = '') as csv_storage:
    b3 = csv.writer(csv_storage)
    b4 = csv.reader(iter(sys.stdin.readline, ''))
    for row in b4:
        b5 = False
        for word in row[1].split():
            if word in b1 and not b5:
                b3.writerow([row[0], row[1]])
                b5 = True
b6 = time.time()