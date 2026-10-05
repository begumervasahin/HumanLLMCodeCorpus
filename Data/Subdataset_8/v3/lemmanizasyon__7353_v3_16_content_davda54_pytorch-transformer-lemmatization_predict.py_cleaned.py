import torch
import argparse
import re
from morpho_dataset import MorphoDataset
from model import Model
VERSION = 'v3.0'
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base_directory", default=".", type=str, help="Directory for the outputs.")
    parser.add_argument("--cle_layers", default=3, type=int, help="Number of CLE embedding layers.")
    parser.add_argument("--cnn_filters", default=96, type=int, help="Number of CNN embedding filters per length.")
    parser.add_argument("--cnn_max_width", default=5, type=int, help="Maximum width of CNN filter.")
    parser.add_argument("--checkpoint", default=None, type=str, help="Path to the model checkpoint.")
    parser.add_argument("--dim", default=296, type=int, help="Dimensionality of hidden layers.")
    parser.add_argument("--dropout", default=0.3, type=float, help="Dropout rate.")
    parser.add_argument("--duz", default=0.1, type=float, help="Davson's Ultimate Forget Rate.")
    parser.add_argument("--heads", default=8, type=int, help="Number of attention heads.")
    parser.add_argument("--label_smoothing", default=0.1, type=float, help="Label smoothing for cross-entropy loss.")
    parser.add_argument("--layers", default=4, type=int, help="Number of attention layers.")
    parser.add_argument("--learning_rate", default=1.0, type=float, help="Initial learning rate multiplier.")
    parser.add_argument("--max_batch_size", default=60 * 1000, type=int, help="Maximum batch size.")
    parser.add_argument("--max_pos_len", default=8, type=int, help="Maximum length of relative positional representation.")
    parser.add_argument("--warmup_steps", default=16000, type=int, help="Warmup steps for learning rate.")
    return parser.parse_args()
def construct_model_directory(args):
    architecture = ",".join(
        ("{}={}".format(re.sub("(.)[^_]*_?", r"\1", key), value) for key, value in sorted(vars(args).items())
         if key not in ["directory", "base_directory", "epochs", "batch_size", "clip_gradient", "checkpoint",
                        "evaluate_each", "max_batch_size", "skip_logging"]))
    return f"{args.base_directory}/models/{VERSION}_{architecture}"
def load_dataset(base_directory):
    return MorphoDataset("czech_pdt", base_directory, add_bow_eow=True)
def load_model(args, num_source_chars, num_target_chars, num_target_tags):
    model = Model(args, num_source_chars, num_target_chars, num_target_tags).cuda()
    checkpoint_path = f"{args.directory}/{args.checkpoint}"
    state = torch.load(checkpoint_path)
    model.load_state_dict(state['state_dict'])
    model.eval()
    return model
def perform_inference(model, test_data, max_batch_size):
    lemma_sentences = []
    tag_sentences = []
    batches_done = 0
    with torch.no_grad():
        for b, (batch, batch_size) in enumerate(test_data.batches(max_batch_size)):
            lemmas, tags = model.predict_to_list(batch, test_data)
            lemma_sentences += lemmas
            tag_sentences += tags
            batches_done += batch_size
            print(f"\r{int(batches_done / test_data.size() * 100):d} %", end='', flush=True)
    return lemma_sentences, tag_sentences
def write_output_to_file(lemma_sentences, tag_sentences, data):
    out_path = "lemmatizer_test.txt"
    with open(out_path, "w", encoding="utf-8") as out_file:
        for i, sentence in enumerate(lemma_sentences):
            for j in range(len(data.data[data.FORMS].word_strings[i])):
                lemma = []
                for c in map(int, sentence[j]):
                    if c == MorphoDataset.Factor.EOW:
                        break
                    lemma.append(data.data[data.LEMMAS].alphabet[c])
                tag = data.data[data.TAGS].words[tag_sentences[i][j]]
                print(data.data[data.FORMS].word_strings[i][j], "".join(lemma), tag, sep="\t", file=out_file)
            print(file=out_file)
def main():
    args = parse_arguments()
    args.directory = construct_model_directory(args)
    morpho = load_dataset(args.base_directory)
    num_source_chars = len(morpho.train.data[morpho.train.FORMS].alphabet)
    num_target_chars = len(morpho.train.data[morpho.train.LEMMAS].alphabet)
    num_target_tags = len(morpho.train.data[morpho.train.TAGS].words)
    network = load_model(args, num_source_chars, num_target_chars, num_target_tags)
    lemma_sentences, tag_sentences = perform_inference(network, morpho.test, args.max_batch_size)
    write_output_to_file(lemma_sentences, tag_sentences, morpho)
    print("\nDone.")
if __name__ == "__main__":
    main()