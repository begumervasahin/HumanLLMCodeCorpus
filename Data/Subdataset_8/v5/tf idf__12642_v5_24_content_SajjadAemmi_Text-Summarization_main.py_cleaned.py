import argparse
from text_summarization import TextSummarization
def main():
    parser = argparse.ArgumentParser(description="Generate a summary of a large text.")
    parser.add_argument("--input", default="io/input/big_text.txt", type=str, help="Path to the input big text file")
    parser.add_argument("--stop-words", default="io/input/stop_words.txt", type=str, help="Path to the stop words file")
    parser.add_argument("--important-words", default="io/input/important_words.txt", type=str, help="Path to the important words file")
    parser.add_argument("--output", default="io/output/small_text.txt", type=str, help="Path to the output small text file")
    args = parser.parse_args()
    summarizer = TextSummarization(args.input, args.stop_words, args.important_words, args.output)
    summarizer.process_text()
    summarizer.summarize_text()
    max_size = input("Enter the maximum size of the small text you want to generate: ")
    summarizer.set_max_size(max_size)
    small_text = summarizer.generate_small_text()
    print(small_text)
    summarizer.write_output()
if __name__ == "__main__":
    main()