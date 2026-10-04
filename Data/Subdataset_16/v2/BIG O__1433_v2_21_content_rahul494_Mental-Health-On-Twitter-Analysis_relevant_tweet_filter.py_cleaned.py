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
    with open('filtered_tweets_per_abused_user.csv', 'w', b2 = '') as csv_file:
        b3 = csv.writer(csv_file)
        b4 = csv.reader(iter(sys.stdin.readline, ''))
        for row in b4:
            tweet_id, b5 = row[0], row[1]
            if any(word.lower() in b1 for word in b5.split()):
                b3.writerow([tweet_id, b5])
if b6 = = "__main__":
    fonk1()