import csv
import sys
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
    for line in sys.stdin:
        tweet_id, b4 = line.strip().split(',')
        b5 = False
        for word in b4.split():
            if word in b1:
                if not b5:
                    b3.writerow([tweet_id, b4])
                    b5 = True
                    break
b6 = time.time() - original_time
print(f"Execution time: {b6} seconds")