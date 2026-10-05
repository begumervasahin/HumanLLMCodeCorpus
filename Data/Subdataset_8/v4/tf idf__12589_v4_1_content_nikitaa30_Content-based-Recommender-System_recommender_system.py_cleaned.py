
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
data_path = "/home/nikita/Downloads/sample-data.csv"
data = pd.read_csv(data_path)
tfidf_vectorizer = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(data['description'])
cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
results = {}
for idx, row in data.iterrows():
    similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
    similar_items = [(cosine_similarities[idx][i], data['id'][i]) for i in similar_indices]
    results[row['id']] = similar_items[1:]
print('Recommendation system setup is complete!')
def get_item_description(item_id):
    return data.loc[data['id'] == item_id]['description'].tolist()[0].split(' - ')[0]
def recommend_similar_items(item_id, num_recommendations):
    print("Recommending " + str(num_recommendations) + " products similar to " + get_item_description(item_id) + "...")
    print("-------")
    recommended_items = results[item_id][:num_recommendations]
    for rec in recommended_items:
        print("Recommended: " + get_item_description(rec[1]) + " (score:" + str(rec[0]) + ")")
recommend_similar_items(item_id=11, num_recommendations=5)