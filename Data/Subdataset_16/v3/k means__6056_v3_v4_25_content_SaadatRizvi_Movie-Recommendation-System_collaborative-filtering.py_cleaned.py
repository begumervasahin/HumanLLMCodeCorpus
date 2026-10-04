import pandas as pd
def fonk1(file_path):
    b1 = ['b19', 'movie_id', 'rating']
    return pd.read_csv(file_path, b2 = '\t', names=b1, usecols=range(3))
def fonk2(file_path):
    b1 = ['movie_id', 'title']
    return pd.read_csv(file_path, b2 = '|', names=b1, usecols=range(2))
def fonk3(b11, b10):
    return pd.merge(b11, b10)
def fonk4(b12):
    return b12.pivot_table(b3 = 'b19', b1='title', values='rating')
def fonk5(b13, b4 = 100):
    return b13.corr(b5 = 'pearson', b4=b4)
def fonk6(b13, b19):
    return b13.loc[b19].dropna()
def fonk7(b15, b14):
    b6 = pd.Series(dtype=float)
    for movie in b15.b3:
        b7 = b14[movie].dropna()
        b7 = b7.map(lambda x: x * b15[movie])
        b6 = b6.append(b7)
    return b6
def fonk8(b6):
    b6 = b6.groupby(b6.b3).sum()
    b6.sort_values(b8 = True, ascending=False)
    return b6
def fonk9(b6, b15):
    return b6.drop(b15.b3, b9 = 'ignore')
def fonk10(ratings_file, movies_file, b19, output_file):
    b10 = fonk1(ratings_file)
    b11 = fonk2(movies_file)
    b12 = fonk3(b11, b10)
    b13 = fonk4(b12)
    b14 = fonk5(b13)
    b15 = fonk6(b13, b19)
    b6 = fonk7(b15, b14)
    b16 = fonk8(b6)
    b17 = fonk9(b16, b15)
    print(b17.head())
    b17.to_csv(output_file)
if b18 = = "__main__":
    fonk10('u.data', 'u.item', b19 = 2, output_file='filteredSims.csv')