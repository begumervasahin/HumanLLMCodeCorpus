import sys
import csv
import time
b1 = [
    'abuse', 'eatingdisorders', 'nostigma', 'presspause', 'addiction', 'endthestigma', 'nostigmas', 'mentalhealthmatters',
    'alzheimers', 'IAmStigmaFree', '1SmallAct', 'ocd', 'anxiety', 'mentalhealth', 'psychology', 'suicideprevention', 'bipolar',
    'pts', 'mhchat', 'therapy', 'bpd', 'schizophrenia', 'trauma', 'Operationalstress', 'ptsd', 'mhsm', 'worldmentalhealthday',
    'AA', 'stress', 'spsm', 'wellbeing', 'alcoholism', 'mentalhealthawareness', 'stopsuicide', 'adhd', 'depressed', 'mentalillness',
    'suicide', 'MH', 'shellshock', 'bts'
]
def fonk1(input_stream, output_file):
    b2 = time.time()
    with open(output_file, 'w', b3 = '') as csv_storage:
        b4 = csv.writer(csv_storage)
        b5 = csv.reader(input_stream)
        for row in b5:
            tweet_id, b6 = row[0], row[1]
            if any(word in b1 for word in b6.split()):
                b4.writerow([tweet_id, b6])
    b7 = time.time() - b2
    print(f"Filtering completed in {b7:.2f} seconds.")
if b8 = = "__main__":
    fonk1(sys.stdin, 'filtered_tweets_per_abused_user.csv')