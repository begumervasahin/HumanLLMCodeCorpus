b1 = pd.read_csv("tmdb_5000_movies.csv",encoding="latin-1")
b1.head(3)
len(b1)
b2 = b1.groupby(['original_title']).agg({'popularity':'count'}).reset_index()
b3 = b1['original_title'].unique()
len(b3)
b4 = b1['original_language'].unique()
b4
from sklearn.feature_extraction.text import TfidfVectorizer
b5 = TfidfVectorizer(stop_words='english')
b1['overview']=b1['overview'].fillna('')
b6 = b5.fit_transform(b1['overview'])
b6.shape
b7 = linear_kernel(b6,b6)
b8 = pd.Series(b1.index,index=b1['original_title']).drop_duplicates()
def fonk1(title,b7 = b7):
    b9 = b8[title]
    b10 = list(enumerate(b7[b9]))
    b10 = sorted(b10,key=lambda x:x[1],reverse=True)
    b10 = b10[1:20]
    b11 = [i[0] for i in b10]
    return b1['original_title'].iloc[b11]
fonk1("No Reservations")