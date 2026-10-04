import argparse
from text_summarization import TextSummarization
def fonk1(b7):
    b1 = TextSummarization(b7.input, b7.stop_words, b7.important_words, b7.output)
    b1.build_matrix()
    b1.remove_stop_words()
    b1.tf_idf()
    b1.search_important_words()
    b1.sum_words_weight_for_sentence_weight()
    b2 = input("Enter the maximum number of words for the output text: ")
    b1.b3 = int(b2)
    b1.create_small_text()
    print(b1.SmallText)
    b1.write_output_file()
if b4 = = "__main__":
    b5 = argparse.ArgumentParser(description="Summarize a large text file based on given parameters.")
    b5.add_argument("--input", b6 = "io/input/big_text.txt", type=str, help="Input big text file path")
    b5.add_argument("--stop-words", b6 = "io/input/stop_words.txt", type=str, help="Stop words file path")
    b5.add_argument("--important-words", b6 = "io/input/important_words.txt", type=str, help="Important words file path")
    b5.add_argument("--output", b6 = "io/output/small_text.txt", type=str, help="Output summarized text file path")
    b7 = b5.parse_args()
    fonk1(b7)