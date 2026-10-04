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
    def RemoveStopWords(self):
        pass
    def Tf_Idf(self):
        pass
    def SearchImportantWords(self):
        pass
    def sum_words_weight_for_sentence_weight(self):
        pass
    def CreateSmallText(self):
        pass
    def write_output_file(self):
        with open(self.output_file, 'w') as file:
            file.write(self.SmallText)
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="io/input/big_text.txt", type=str, help="input big text")
    parser.add_argument("--stop-words", default="io/input/stop_words.txt", type=str, help="input stop words")
    parser.add_argument("--important-words", default="io/input/important_words.txt", type=str, help="input important words")
    parser.add_argument("--output", default="io/output/small_text.txt", type=str, help="output small text")
    args = parser.parse_args()
    TS = TextSummarization(args.input, args.stop_words, args.important_words, args.output)
    TS.build_matrix()
    TS.RemoveStopWords()
    TS.Tf_Idf()
    TS.SearchImportantWords()
    TS.sum_words_weight_for_sentence_weight()
    TS.MaxSizeOfSmallText = int(input("Enter the maximum number of words for the output text: "))
    TS.CreateSmallText()
    print(TS.SmallText)
    TS.write_output_file()