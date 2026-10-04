import sys
import csv
import time
KEYWORDS = [
    'abuse', 'eatingdisorders', 'nostigma', 'presspause', 'addiction', 'endthestigma', 'nostigmas', 'mentalhealthmatters',
    'alzheimers', 'IAmStigmaFree', '1SmallAct', 'ocd', 'anxiety', 'mentalhealth', 'psychology', 'suicideprevention', 'bipolar',
    'pts', 'mhchat', 'therapy', 'bpd', 'schizophrenia', 'trauma', 'Operationalstress', 'ptsd', 'mhsm', 'worldmentalhealthday',
    'AA', 'stress', 'spsm', 'wellbeing', 'alcoholism', 'mentalhealthawareness', 'stopsuicide', 'adhd', 'depressed', 'mentalillness',
    'suicide', 'MH', 'shellshock', 'bts'
]
def filter_tweets(input_stream, output_file):
    start_time = time.time()
    with open(output_file, 'w', newline='') as csv_storage:
        csv_writer = csv.writer(csv_storage)
        data = csv.reader(input_stream)
        for row in data:
            tweet_id, tweet_text = row[0], row[1]
            if any(word in KEYWORDS for word in tweet_text.split()):
                csv_writer.writerow([tweet_id, tweet_text])
    elapsed_time = time.time() - start_time
    print(f"Filtering completed in {elapsed_time:.2f} seconds.")
if __name__ == "__main__":
    filter_tweets(sys.stdin, 'filtered_tweets_per_abused_user.csv')