import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
def find_cosine_similarities(tweets, vectorizer, tdm):
    cosine_similarities_map = []
    for tweet in tweets:
        related_tweets = []
        query = vectorizer.transform([tweet])
        cosine_similarities = linear_kernel(query, tdm).flatten()
        related_docs_indices = cosine_similarities.argsort()[:-5:-1]
        for index in related_docs_indices:
            related_tweets.append((tweets[index], cosine_similarities[index]))
        cosine_similarities_map.append({tweet: related_tweets})
    return cosine_similarities_map
def main():
    with open('tweets.txt', 'r') as file:
        tweets = file.readlines()
    vectorizer = TfidfVectorizer(analyzer="word")
    term_document_matrix = vectorizer.fit_transform(tweets)
    similarities_map = find_cosine_similarities(tweets, vectorizer, term_document_matrix)
    data = {'tweet_one': [], 'tweet_two': [], 'cosine_similarity': []}
    for tweet_map in similarities_map:
        for tweet, related_tweets in tweet_map.items():
            for related_tweet, cosine_similarity in related_tweets:
                if tweet != related_tweet:
                    data['tweet_one'].append(tweet)
                    data['tweet_two'].append(related_tweet)
                    data['cosine_similarity'].append(cosine_similarity)
    df = pd.DataFrame(data)
    df.to_csv('tweet_cosine_similarities.csv', index=False)
if __name__ == "__main__":
    main()