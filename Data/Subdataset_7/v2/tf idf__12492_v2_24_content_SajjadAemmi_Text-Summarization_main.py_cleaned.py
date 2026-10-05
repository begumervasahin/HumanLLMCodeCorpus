import argparse
from text_summarization import TextSummarization
def fonk1():
    b1 = argparse.ArgumentParser(description="Summarize a large text")
    b1.add_argument("--input", b2 = "io/input/big_text.txt", type=str, help="Path to the input big text file")
    b1.add_argument("--stop-words", b2 = "io/input/stop_words.txt", type=str, help="Path to the stop words file")
    b1.add_argument("--important-words", b2 = "io/input/important_words.txt", type=str, help="Path to the important words file")
    b1.add_argument("--output", b2 = "io/output/small_text.txt", type=str, help="Path to save the output small text file")
    b3 = b1.parse_args()
    b4 = TextSummarization(b3.input, b3.stop_words, b3.important_words, b3.output)
    b4.build_matrix()
    b4.RemoveStopWords()
    b4.Tf_Idf()
    b4.SearchImportantWords()
    b4.sum_words_weight_for_sentence_weight()
    b4.b5 = input("Enter the maximum number of sentences for the summary: ")
    b4.CreateSmallText()
    print("Summary:")
    print(b4.SmallText)
    b4.write_output_file()
if b6 = = "__main__":
    fonk1()