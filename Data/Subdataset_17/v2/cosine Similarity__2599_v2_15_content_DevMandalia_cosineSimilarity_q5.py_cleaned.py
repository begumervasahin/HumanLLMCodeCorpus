import distsim
def display_nearest_words(word, word_to_vec_dict):
    print(f"Word is:::: {word}")
    nearest_words = distsim.show_nearest(
        word_to_vec_dict,
        word_to_vec_dict[word],
        set([word]),
        distsim.cossim_dense
    )
    for i, (nearest_word, score) in enumerate(nearest_words):
        print(f"{i}: {nearest_word} ({score})")
    print("--------------------")
def main():
    word_to_vec_dict = distsim.load_word2vec("nyt_word2vec.4k")
    words_to_check = ["america", "years", "great", "run", "between", "wife"]
    for word in words_to_check:
        display_nearest_words(word, word_to_vec_dict)
if __name__ == "__main__":
    main()