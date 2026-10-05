import csv
import sys
import time
keywords = ['abuse', 'eatingdisorders', 'nostigma', 'presspause', 'addiction', 'endthestigma', 'nostigmas',
            'mentalhealthmatters', 'alzheimers', 'IAmStigmaFree', '1SmallAct', 'ocd', 'anxiety', 'mentalhealth',
            'psychology', 'suicideprevention', 'bipolar', 'pts', 'mhchat', 'therapy', 'bpd', 'anxiety', 'schizophrenia',
            'trauma', 'Operationalstress', 'therapy', 'ptsd', 'mhsm', 'endthestigma', 'psychology', 'worldmentalhealthday',
            'trauma', 'AA', 'schizophrenia', 'stress', 'spsm', 'mentalhealthmatters', 'stigma', 'wellbeing', 'alcoholism',
            'mentalhealthawareness', 'stopsuicide', 'adhd', 'depressed', 'mentalillness', 'suicide', 'bpd', 'depression', 'MH',
            'shellshock', 'bts']
with open('filtered_tweets_per_abused_user.csv', 'w', newline='') as csv_storage:
    csv_writer = csv.writer(csv_storage)
    for line in sys.stdin:
        tweet_id, tweet_text = line.strip().split(',')
        added = False
        for word in tweet_text.split():
            if word in keywords:
                if not added:
                    csv_writer.writerow([tweet_id, tweet_text])
                    added = True
execution_time = time.time() - original_time
print(f"Execution time: {execution_time} seconds")