import os
import pickle
import torch
from torch.optim import Adam
from torch.utils.data import DataLoader
from tqdm import tqdm
from DataHandler import pad_word, TextLoader, SkipGramData, write_embedding
from Model import SkipGram
import config
def create_directories(directories):
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
def load_existing_data():
    data_files = ['corpus', 'word_count', 'word_freq', 'vocab', 'idx2word', 'word2idx']
    data = {}
    for file in data_files:
        with open(os.path.join('data', f'{file}.dat'), 'rb') as f:
            data[file] = pickle.load(f)
    print(f"\nContinuing training from previous state for {config.epochs} epochs ...")
    return data
def initialize_new_data():
    textloader = TextLoader(
        corpus_file=config.corpus_file,
        max_vocab_size=int(config.max_vocab_size),
        max_corpus_size=int(config.max_corpus_size),
        fw_subsampling_th=config.fw_subsampling_th
    )
    corpus, idx2word, word2idx, vocab, word_count, word_freq = textloader.load_corpus()
    data_to_save = {
        'corpus': corpus,
        'word_count': word_count,
        'word_freq': word_freq,
        'vocab': vocab,
        'idx2word': idx2word,
        'word2idx': word2idx
    }
    for name, data in data_to_save.items():
        with open(os.path.join('data', f'{name}.dat'), 'wb') as f:
            pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"\nTraining for {config.epochs} epochs ...")
    return data_to_save
def initialize_model(data, device):
    skipgram = SkipGram(
        vocab_size=len(data['idx2word']),
        embedding_dims=config.embedding_dims,
        neg_samples=config.neg_samples,
        word_freq=data['word_freq'],
        padding_idx=data['word2idx'][pad_word]
    )
    return skipgram.to(device=device)
def load_model_and_optimizer(skipgram, optim):
    skipgram.load_state_dict(torch.load(os.path.join('model', 'model.pt')))
    optim.load_state_dict(torch.load(os.path.join('model', 'optimizer.pt')))
def train_model(skipgram, optim, dataloader, device):
    for epoch in range(1, config.epochs + 1):
        pbar = tqdm(dataloader, desc=f"[Epoch {epoch}]")
        for targets, contexts in pbar:
            targets, contexts = targets.to(dtype=torch.long, device=device), contexts.to(dtype=torch.long, device=device)
            loss = skipgram(targets, contexts)
            optim.zero_grad()
            loss.backward()
            optim.step()
            pbar.set_postfix(loss=loss.item())
        torch.save(skipgram.state_dict(), os.path.join('model', 'model.pt'))
        torch.save(optim.state_dict(), os.path.join('model', 'optimizer.pt'))
        input_idx2vec = skipgram.input_embedding.weight.data.cpu().numpy()
        output_idx2vec = skipgram.output_embedding.weight.data.cpu().numpy()
        write_embedding(os.path.join('embeddings', 'input_embeddings.txt'), data['idx2word'], data['word2idx'], input_idx2vec)
        write_embedding(os.path.join('embeddings', 'output_embeddings.txt'), data['idx2word'], data['word2idx'], output_idx2vec)
def main():
    create_directories(['model', 'embeddings', 'data'])
    if config.cont_traning:
        data = load_existing_data()
    else:
        data = initialize_new_data()
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    skipgram = initialize_model(data, device)
    optim = Adam(skipgram.parameters())
    if config.cont_traning:
        load_model_and_optimizer(skipgram, optim)
    dataset = SkipGramData(data['corpus'], data['word2idx'], window=config.window_size)
    dataloader = DataLoader(dataset, batch_size=config.mini_batch_size, shuffle=True)
    train_model(skipgram, optim, dataloader, device)
if __name__ == "__main__":
    main()