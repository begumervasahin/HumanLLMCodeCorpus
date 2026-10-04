from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
b1 = "Mr. Trump became president after winning the political election. Though he lost the support of some republican friends, Trump is friends with President Putin"
b2 = "President Trump says Putin had no political interference is the election outcome. He says it was a witchhunt by political parties. He claimed President Putin is a friend who had nothing to do with the election"
b3 = "Post elections, Vladimir Putin became President of Russia. President Putin had served as the Prime Minister earlier in his political career"
b4 = [b1, b2, b3]
b5 = CountVectorizer(stop_words='english')
b6 = b5.fit_transform(b4)
b7 = b6.todense()
b8 = pd.DataFrame(b7, columns=b5.get_feature_names(), index=['b1', 'b2', 'b3'])
print("Document-Term Matrix:")
print(b8)
b9 = cosine_similarity(b8, b8)
print("\nCosine Similarity Matrix:")
print(b9)