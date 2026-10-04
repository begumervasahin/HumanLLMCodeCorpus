import sys
import csv
b1 = [
    'abuse', 'eatingdisorders', 'nostigma', 'presspause', 'addiction',
    'endthestigma', 'nostigmas', 'mentalhealthmatters', 'alzheimers',
    'IAmStigmaFree', '1SmallAct', 'ocd', 'anxiety', 'mentalhealth',
    'psychology', 'suicideprevention', 'bipolar', 'pts', 'mhchat',
    'therapy', 'bpd', 'schizophrenia', 'trauma', 'Operationalstress',
    'ptsd', 'mhsm', 'worldmentalhealthday', 'AA', 'stress', 'spsm',
    'wellbeing', 'alcoholism', 'mentalhealthawareness', 'stopsuicide',
    'adhd', 'depressed', 'mentalillness', 'suicide', 'MH', 'shellshock',
    'bts'
]
def fonk1(b7):
    b2 = b7.lower().split()
    return any(keyword in b2 for keyword in b1)
def fonk2():
    b3 = 'filtered_tweets_per_abused_user.csv'
    with open(b3, 'w', b4 = '') as csv_file:
        b5 = csv.writer(csv_file)
        b6 = csv.reader(iter(sys.stdin.readline, ''))
        for row in b6:
            tweet_id, b7 = row[0], row[1]
            if fonk1(b7):
                b5.writerow([tweet_id, b7])
if b8 = = "__main__":
    fonk2()