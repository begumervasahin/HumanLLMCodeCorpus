import os
import pickle
import torch
from torch.optim import Adam
from torch.utils.data import DataLoader
from tqdm import tqdm
from DataHandler import pad_word, TextLoader, SkipGramData, write_embedding
from Model import SkipGram
import config
def ensure_directories_exist(dirs):
    for directory in dirs:
        os.makedirs(directory, exist_ok=True)
def load_training_state(data_dir):
    with open(os.path.join(data_dir, 'corpus.dat'), 'rb') as f:
        corpus = pickle.load(f)
    with open(os.path.join(data_dir, 'word_count.dat'), 'rb') as f:
        word_count = pickle.load(f)
    with open(os.path.join(data_dir, 'word_freq.dat'), 'rb') as f:
        word_freq = pickle.load(f)
    with open(os.path.join(data_dir, 'vocab.dat'), 'rb') as f:
        vocab = pickle.load(f)
    with open(os.path.join(data_dir, 'idx2word.dat'), 'rb') as f:
        idx2word = pickle.load(f)
    with open(os.path.join(data_dir, 'word2idx.dat'), 'rb') as f:
        word2idx = pickle.load(f)
    return corpus, word_count, word_freq, vocab, idx2word, word2idx
def save_training_state(data_dir, state_dict):
    for name, data in state_dict.items():
        with open(os.path.join(data_dir, f'{name}.dat'), 'wb') as f:
            pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
def initialize_corpus_and_vocab():
    textloader = TextLoader(
        corpus_file=config.corpus_file,
        max_vocab_size=int(config.max_vocab_size),
        max_corpus_size=int(config.max_corpus_size),
        fw_subsampling_th=config.fw_subsampling_th
    )
    return textloader.load_corpus()
def prepare_data_loader(corpus, word2idx):
    dataset = SkipGramData(corpus, word2idx, window=config.window_size)
    return DataLoader(dataset, batch_size=config.mini_batch_size, shuffle=True)
def save_embeddings(embeddings_dir, skipgram, idx2word, word2idx):
    input_embeddings = skipgram.input_embedding.weight.data.cpu().numpy()
    output_embeddings = skipgram.output_embedding.weight.data.cpu().numpy()
    write_embedding(os.path.join(embeddings_dir, 'input_embeddings.txt'), idx2word, word2idx, input_embeddings)
    write_embedding(os.path.join(embeddings_dir, 'output_embeddings.txt'), idx2word, word2idx, output_embeddings)
def main():
    ensure_directories_exist(['model', 'embeddings', 'data'])
    if config.cont_training:
        corpus, word_count, word_freq, vocab, idx2word, word2idx = load_training_state('data')
        print(f"\nContinuing training from previous state for {config.epochs} epochs ...")
    else:
        corpus, idx2word, word2idx, vocab, word_count, word_freq = initialize_corpus_and_vocab()
        save_training_state('data', {
            'corpus': corpus,
            'word_count': word_count,
            'word_freq': word_freq,
            'vocab': vocab,
            'idx2word': idx2word,
            'word2idx': word2idx
        })
        print(f"\nTraining for {config.epochs} epochs ...")
    skipgram = SkipGram(
        vocab_size=len(idx2word),
        embedding_dims=config.embedding_dims,
        neg_samples=config.neg_samples,
        word_freq=word_freq,
        padding_idx=word2idx[pad_word]
    )
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    skipgram.to(device=device)
    optimizer = Adam(skipgram.parameters())
    if config.cont_training:
        skipgram.load_state_dict(torch.load(os.path.join('model', 'model.pt')))
        optimizer.load_state_dict(torch.load(os.path.join('model', 'optimizer.pt')))
    dataloader = prepare_data_loader(corpus, word2idx)
    for epoch in range(1, config.epochs + 1):
        pbar = tqdm(dataloader, desc=f"[Epoch {epoch}]")
        for targets, contexts in pbar:
            targets = targets.to(dtype=torch.long, device=device)
            contexts = contexts.to(dtype=torch.long, device=device)
            loss = skipgram(targets, contexts)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            pbar.set_postfix(loss=loss.item())
        torch.save(skipgram.state_dict(), os.path.join('model', 'model.pt'))
        torch.save(optimizer.state_dict(), os.path.join('model', 'optimizer.pt'))
        save_embeddings('embeddings', skipgram, idx2word, word2idx)
if __name__ == "__main__":
    main()