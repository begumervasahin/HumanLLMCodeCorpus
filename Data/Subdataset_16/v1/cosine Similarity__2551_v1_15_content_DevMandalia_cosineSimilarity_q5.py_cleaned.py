import distsim
def fonk1(word, b2):
    print(f"Word is:::: {word}")
    b1 = distsim.show_nearest(
        b2,
        b2[word],
        set([word]),
        distsim.cossim_dense
    )
    for i, (nearest_word, score) in enumerate(b1):
        print(f"{i}: {nearest_word} ({score})")
    print("--------------------")
def fonk2():
    b2 = distsim.load_word2vec("nyt_word2vec.4k")
    b3 = ["america", "years", "great", "run", "between", "wife"]
    for word in b3:
        fonk1(word, b2)
if b4 = = "__main__":
    fonk2()