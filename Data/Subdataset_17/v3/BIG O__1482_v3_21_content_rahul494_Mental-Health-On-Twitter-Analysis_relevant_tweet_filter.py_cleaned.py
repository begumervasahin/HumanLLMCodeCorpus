import sys
import csv
KEYWORDS = [
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
def contains_keywords(tweet_text):
    tweet_words = tweet_text.lower().split()
    return any(keyword in tweet_words for keyword in KEYWORDS)
def filter_tweets():
    output_file = 'filtered_tweets_per_abused_user.csv'
    with open(output_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        data = csv.reader(iter(sys.stdin.readline, ''))
        for row in data:
            tweet_id, tweet_text = row[0], row[1]
            if contains_keywords(tweet_text):
                csv_writer.writerow([tweet_id, tweet_text])
if __name__ == "__main__":
    filter_tweets()