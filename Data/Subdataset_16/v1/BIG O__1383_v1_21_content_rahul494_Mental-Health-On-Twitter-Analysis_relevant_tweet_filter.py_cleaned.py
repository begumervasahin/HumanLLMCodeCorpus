import sys
import csv
import time
b1 = [
    'abuse', 'eatingdisorders', 'nostigma', 'presspause', 'addiction',
    'endthestigma', 'nostigmas', 'mentalhealthmatters', 'alzheimers',
    'IAmStigmaFree', '1SmallAct', 'ocd', 'anxiety', 'mentalhealth',
    'psychology', 'suicideprevention', 'bipolar', 'pts', 'mhchat',
    'therapy', 'bpd', 'anxiety', 'schizophrenia', 'trauma',
    'Operationalstress', 'therapy', 'ptsd', 'mhsm', 'endthestigma',
    'psychology', 'worldmentalhealthday', 'trauma', 'AA', 'schizophrenia',
    'stress', 'spsm', 'mentalhealthmatters', 'stigma', 'wellbeing',
    'alcoholism', 'mentalhealthawareness', 'stopsuicide', 'adhd',
    'depressed', 'mentalillness', 'suicide', 'bpd', 'depression', 'MH',
    'shellshock', 'bts'
]
def fonk1():
    with open('filtered_tweets_per_abused_user.csv', 'w', b2 = '') as csvStorage:
        b3 = time.time()
        b4 = csv.writer(csvStorage)
        b5 = csv.reader(iter(sys.stdin.readline, ''))
        for row in b5:
            b6 = False
            for word in row[1].split():
                if word.lower() in b1:
                    if not b6:
                        b4.writerow([row[0], row[1]])
                        b6 = True
                        break
if b7 = = "__main__":
    fonk1()