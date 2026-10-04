import argparse
from text_summarization import TextSummarization
def fonk1(b11):
    b1 = TextSummarization(
        b2 = b11.input,
        b3 = b11.stop_words,
        b4 = b11.important_words,
        b5 = b11.output
    )
    b1.build_matrix()
    b1.remove_stop_words()
    b1.calculate_tf_idf()
    b1.search_important_words()
    b1.sum_words_weight_for_sentence_weight()
    b6 = int(input("Enter the maximum number of words for the output text: "))
    b1.b7 = b6
    b1.create_small_text()
    print(b1.SmallText)
    b1.write_output_file()
def fonk2():
    b8 = argparse.ArgumentParser(description="Summarize a large text file based on given parameters.")
    b8.add_argument("--input", b9 = "io/input/big_text.txt", type=str, help="Input big text file path")
    b8.add_argument("--stop-words", b9 = "io/input/stop_words.txt", type=str, help="Stop words file path")
    b8.add_argument("--important-words", b9 = "io/input/important_words.txt", type=str, help="Important words file path")
    b8.add_argument("--output", b9 = "io/output/small_text.txt", type=str, help="Output summarized text file path")
    return b8.parse_args()
if b10 = = "__main__":
    b11 = fonk2()
    fonk1(b11)