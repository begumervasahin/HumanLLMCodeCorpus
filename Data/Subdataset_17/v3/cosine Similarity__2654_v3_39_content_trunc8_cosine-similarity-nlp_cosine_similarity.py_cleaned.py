from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
doc_trump = "Mr. Trump became president after winning the political election. Though he lost the support of some republican friends, Trump is friends with President Putin"
doc_election = "President Trump says Putin had no political interference in the election outcome. He says it was a witchhunt by political parties. He claimed President Putin is a friend who had nothing to do with the election"
doc_putin = "Post elections, Vladimir Putin became President of Russia. President Putin had served as the Prime Minister earlier in his political career"
documents = [doc_trump, doc_election, doc_putin]
count_vectorizer = CountVectorizer(stop_words='english')
doc_term_matrix = count_vectorizer.fit_transform(documents).todense()
df = pd.DataFrame(doc_term_matrix, columns=count_vectorizer.get_feature_names(), index=['doc_trump', 'doc_election', 'doc_putin'])
print("Document-Term Matrix:")
print(df)
cosine_sim = cosine_similarity(df, df)
print("\nCosine Similarity Matrix:")
print(cosine_sim)