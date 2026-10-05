import sys
import csv
import time
keywords = ['abuse', 'eatingdisorders', 'nostigma', 'presspause', 'addiction', 'endthestigma', 'nostigmas',
            'mentalhealthmatters', 'alzheimers', 'IAmStigmaFree', '1SmallAct', 'ocd', 'anxiety', 'mentalhealth',
            'psychology', 'suicideprevention', 'bipolar', 'pts', 'mhchat', 'therapy', 'bpd', 'anxiety', 'schizophrenia',
            'trauma', 'Operationalstress', 'therapy', 'ptsd', 'mhsm', 'endthestigma', 'psychology', 'worldmentalhealthday',
            'trauma', 'AA', 'schizophrenia', 'stress', 'spsm', 'mentalhealthmatters', 'stigma', 'wellbeing', 'alcoholism',
            'mentalhealthawareness', 'stopsuicide', 'adhd', 'depressed', 'mentalillness', 'suicide', 'bpd', 'depression', 'MH',
            'shellshock', 'bts']
with open('filtered_tweets_per_abused_user.csv', 'w', newline='') as csvStorage:
    csv_writer = csv.writer(csvStorage)
    data = csv.reader(iter(sys.stdin.readline, ''))
    for row in data:
        added = False
        for word in row[1].split():
            if word in keywords:
                if not added:
                    csv_writer.writerow([row[0], row[1]])
                    added = True
original_time = time.time()