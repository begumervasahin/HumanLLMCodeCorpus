import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
dataset_path = "/home/nikita/Downloads/sample-data.csv"
ds = pd.read_csv(dataset_path)
tfidf_vectorizer = TfidfVectorizer(
    analyzer='word',
    ngram_range=(1, 3),
    min_df=0,
    stop_words='english'
)
tfidf_matrix = tfidf_vectorizer.fit_transform(ds['description'])
cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
results = {}
for idx, row in ds.iterrows():
    similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
    similar_items = [
        (cosine_similarities[idx][i], ds['id'][i])
        for i in similar_indices
    ]
    results[row['id']] = similar_items[1:]
print('done!')
def get_item_description(item_id):
    description = ds.loc[ds['id'] == item_id, 'description'].values[0]
    return description.split(' - ')[0]
def recommend_items(item_id, num_recommendations):
    print(f"Recommending {num_recommendations} products similar to {get_item_description(item_id)}...")
    print("-------")
    recommendations = results[item_id][:num_recommendations]
    for score, recommended_item_id in recommendations:
        print(f"Recommended: {get_item_description(recommended_item_id)} (score: {score})")
recommend_items(item_id=11, num_recommendations=5)