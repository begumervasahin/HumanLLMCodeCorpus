import argparse
from text_summarization import TextSummarization
def fonk1():
    b1 = argparse.ArgumentParser(description="Generate a summary of a large text.")
    b1.add_argument("--input", b2 = "io/input/big_text.txt", type=str, help="Path to the input big text file")
    b1.add_argument("--stop-words", b2 = "io/input/stop_words.txt", type=str, help="Path to the stop words file")
    b1.add_argument("--important-words", b2 = "io/input/important_words.txt", type=str, help="Path to the important words file")
    b1.add_argument("--output", b2 = "io/output/b6.txt", type=str, help="Path to the output small text file")
    b3 = b1.parse_args()
    b4 = TextSummarization(b3.input, b3.stop_words, b3.important_words, b3.output)
    b4.process_text()
    b4.summarize_text()
    b5 = input("Enter the maximum size of the small text you want to generate: ")
    b4.set_max_size(b5)
    b6 = b4.generate_small_text()
    print(b6)
    b4.write_output()
if b7 = = "__main__":
    fonk1()