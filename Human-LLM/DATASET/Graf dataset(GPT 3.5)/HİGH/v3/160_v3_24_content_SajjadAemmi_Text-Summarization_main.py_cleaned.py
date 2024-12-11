import argparse
from text_summarization import TextSummarization
def fonk1(input_path, stop_words_path, important_words_path, output_path):
    b1 = TextSummarization(input_path, stop_words_path, important_words_path, output_path)
    b1.build_matrix()
    b1.RemoveStopWords()
    b1.Tf_Idf()
    b1.SearchImportantWords()
    b1.sum_words_weight_for_sentence_weight()
    b2 = input("Enter the maximum number of sentences for the summary: ")
    b1.b3 = b2
    b1.CreateSmallText()
    print("Summary:")
    print(b1.SmallText)
    b1.write_output_file()
def fonk2():
    b4 = argparse.ArgumentParser(description="Summarize a large text")
    b4.add_argument("--input", b5 = "io/input/big_text.txt", type=str, help="Path to the input big text file")
    b4.add_argument("--stop-words", b5 = "io/input/stop_words.txt", type=str, help="Path to the stop words file")
    b4.add_argument("--important-words", b5 = "io/input/important_words.txt", type=str, help="Path to the important words file")
    b4.add_argument("--output", b5 = "io/output/small_text.txt", type=str, help="Path to save the output small text file")
    b6 = b4.parse_args()
    fonk1(b6.input, b6.stop_words, b6.important_words, b6.output)
if b7 = = "__main__":
    fonk2()