import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
dataset = pd.read_csv("/home/nikita/Downloads/sample-data.csv")
tfidf_vectorizer = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(dataset['description'])
cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
similar_results = {}
for idx, row in dataset.iterrows():
    similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
    similar_items = [(cosine_similarities[idx][i], dataset['id'][i]) for i in similar_indices]
    similar_results[row['id']] = similar_items[1:]
print('Similarity computation done!')
def get_item_description(item_id):
    return dataset.loc[dataset['id'] == item_id]['description'].tolist()[0].split(' - ')[0]
def recommend_similar_items(item_id, num_recommendations):
    print("Recommending " + str(num_recommendations) + " products similar to " + get_item_description(item_id) + "...")
    print("-------")
    recommendations = similar_results[item_id][:num_recommendations]
    for recommendation in recommendations:
        print("Recommended: " + get_item_description(recommendation[1]) + " (score:" + str(recommendation[0]) + ")")
recommend_similar_items(item_id=11, num_recommendations=5)