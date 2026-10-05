import argparse
from text_summarization import TextSummarization
def main():
    parser = argparse.ArgumentParser(description="Summarize a large text")
    parser.add_argument("--input", default="io/input/big_text.txt", type=str, help="Path to the input big text file")
    parser.add_argument("--stop-words", default="io/input/stop_words.txt", type=str, help="Path to the stop words file")
    parser.add_argument("--important-words", default="io/input/important_words.txt", type=str, help="Path to the important words file")
    parser.add_argument("--output", default="io/output/small_text.txt", type=str, help="Path to save the output small text file")
    args = parser.parse_args()
    summarizer = TextSummarization(args.input, args.stop_words, args.important_words, args.output)
    summarizer.build_matrix()
    summarizer.RemoveStopWords()
    summarizer.Tf_Idf()
    summarizer.SearchImportantWords()
    summarizer.sum_words_weight_for_sentence_weight()
    summarizer.MaxSizeOfSmallText = input("Enter the maximum number of sentences for the summary: ")
    summarizer.CreateSmallText()
    print("Summary:")
    print(summarizer.SmallText)
    summarizer.write_output_file()
if __name__ == "__main__":
    main()