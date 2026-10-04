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
def main():
    parser = argparse.ArgumentParser(description="Summarize a large text file into a smaller one based on important words.")
    parser.add_argument("--input", default="io/input/big_text.txt", type=str, help="Path to the input big text file")
    parser.add_argument("--stop-words", default="io/input/stop_words.txt", type=str, help="Path to the stop words file")
    parser.add_argument("--important-words", default="io/input/important_words.txt", type=str, help="Path to the important words file")
    parser.add_argument("--output", default="io/output/small_text.txt", type=str, help="Path to the output small text file")
    args = parser.parse_args()
    TS = TextSummarization(args.input, args.stop_words, args.important_words, args.output)
    TS.build_matrix()
    TS.remove_stop_words()
    TS.calculate_tf_idf()
    TS.search_important_words()
    TS.sum_words_weight_for_sentence_weight()
    TS.MaxSizeOfSmallText = int(input("Enter the maximum number of words for the output text: "))
    TS.create_small_text()
    print(TS.SmallText)
    TS.write_output_file()
if __name__ == "__main__":
    main()