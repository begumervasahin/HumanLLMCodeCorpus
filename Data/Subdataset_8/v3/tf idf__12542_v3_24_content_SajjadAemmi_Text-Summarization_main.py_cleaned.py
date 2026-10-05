import argparse
from text_summarization import TextSummarization
def summarize_text(input_path, stop_words_path, important_words_path, output_path):
    summarizer = TextSummarization(input_path, stop_words_path, important_words_path, output_path)
    summarizer.build_matrix()
    summarizer.RemoveStopWords()
    summarizer.Tf_Idf()
    summarizer.SearchImportantWords()
    summarizer.sum_words_weight_for_sentence_weight()
    max_sentences = input("Enter the maximum number of sentences for the summary: ")
    summarizer.MaxSizeOfSmallText = max_sentences
    summarizer.CreateSmallText()
    print("Summary:")
    print(summarizer.SmallText)
    summarizer.write_output_file()
def main():
    parser = argparse.ArgumentParser(description="Summarize a large text")
    parser.add_argument("--input", default="io/input/big_text.txt", type=str, help="Path to the input big text file")
    parser.add_argument("--stop-words", default="io/input/stop_words.txt", type=str, help="Path to the stop words file")
    parser.add_argument("--important-words", default="io/input/important_words.txt", type=str, help="Path to the important words file")
    parser.add_argument("--output", default="io/output/small_text.txt", type=str, help="Path to save the output small text file")
    args = parser.parse_args()
    summarize_text(args.input, args.stop_words, args.important_words, args.output)
if __name__ == "__main__":
    main()