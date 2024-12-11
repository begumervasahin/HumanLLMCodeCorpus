import argparse
from text_summarization import TextSummarization
b1 = argparse.ArgumentParser()
b1.add_argument("--input", b2 = "io/input/big_text.txt", type=str, help="input big text")
b1.add_argument("--stop-words", b2 = "io/input/stop_words.txt", type=str, help="input stop words")
b1.add_argument("--important-words", b2 = "io/input/important_words.txt", type=str, help="input important words")
b1.add_argument("--output", b2 = "io/output/small_text.txt", type=str, help="output small text")
b3 = b1.parse_args()
if b4 = = "__main__":
    b5 = TextSummarization(b3.input, b3.stop_words, b3.important_words, b3.output)
    b5.build_matrix()
    b5.RemoveStopWords()
    b5.Tf_Idf()
    b5.SearchImportantWords()
    b5.sum_words_weight_for_sentence_weight()
    b5.b6 = input("Ø­Ø¯Ø§Ú©Ø«Ø± ØªØ¹Ø¯Ø§Ø¯ Ú©ÙÙ
Ø§Øª Ù
ØªÙ Ø®Ø±ÙØ¬Û Ø±Ø§ ÙØ§Ø±Ø¯ ÙÙ
Ø§ÛÛØ¯: ")
    b5.CreateSmallText()
    print(b5.SmallText)
    b5.write_output_file()