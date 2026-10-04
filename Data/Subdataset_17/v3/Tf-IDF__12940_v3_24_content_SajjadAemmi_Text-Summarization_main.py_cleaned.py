import argparse
class TextSummarization:
    def __init__(self, input_file, stop_words_file, important_words_file, output_file):
        self.input_file = input_file
        self.stop_words_file = stop_words_file
        self.important_words_file = important_words_file
        self.output_file = output_file
        self.SmallText = ""
        self.MaxSizeOfSmallText = 0
    def build_matrix(self):
        pass
    def remove_stop_words(self):
        pass
    def calculate_tf_idf(self):
        pass
    def search_important_words(self):
        pass
    def sum_words_weight_for_sentence_weight(self):
        pass
    def create_small_text(self):
        pass
    def write_output_file(self):
        with open(self.output_file, 'w') as file:
            file.write(self.SmallText)
def parse_arguments():
    parser = argparse.ArgumentParser(description="Summarize a large text file into a smaller one based on important words.")
    parser.add_argument("--input", default="io/input/big_text.txt", type=str, help="Path to the input big text file")
    parser.add_argument("--stop-words", default="io/input/stop_words.txt", type=str, help="Path to the stop words file")
    parser.add_argument("--important-words", default="io/input/important_words.txt", type=str, help="Path to the important words file")
    parser.add_argument("--output", default="io/output/small_text.txt", type=str, help="Path to the output small text file")
    return parser.parse_args()
def main():
    args = parse_arguments()
    text_summarizer = TextSummarization(args.input, args.stop_words, args.important_words, args.output)
    text_summarizer.build_matrix()
    text_summarizer.remove_stop_words()
    text_summarizer.calculate_tf_idf()
    text_summarizer.search_important_words()
    text_summarizer.sum_words_weight_for_sentence_weight()
    text_summarizer.MaxSizeOfSmallText = int(input("Enter the maximum number of words for the output text: "))
    text_summarizer.create_small_text()
    print(text_summarizer.SmallText)
    text_summarizer.write_output_file()
if __name__ == "__main__":
    main()