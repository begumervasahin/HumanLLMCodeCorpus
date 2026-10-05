import os
import pickle
import torch
from torch.optim import Adam
from torch.utils.data import DataLoader
from tqdm import tqdm
from DataHandler import pad_word, TextLoader, SkipGramData, write_embedding
from Model import SkipGram
import config
for directory in ['model', 'embeddings', 'data']:
    if not os.path.isdir(directory):
        os.mkdir(directory)
if config.cont_training:
    print("\nContinuing training from previous state for {} epochs...".format(config.epochs))
    with open(os.path.join('data', 'corpus.dat'), 'rb') as f:
        corpus = pickle.load(f)
    with open(os.path.join('data', 'word_count.dat'), 'rb') as f:
        word_count = pickle.load(f)
    with open(os.path.join('data', 'word_freq.dat'), 'rb') as f:
        word_freq = pickle.load(f)
    with open(os.path.join('data', 'vocab.dat'), 'rb') as f:
        vocab = pickle.load(f)
    with open(os.path.join('data', 'idx2word.dat'), 'rb') as f:
        idx2word = pickle.load(f)
    with open(os.path.join('data', 'word2idx.dat'), 'rb') as f:
        word2idx = pickle.load(f)
else:
    textloader = TextLoader(corpus_file=config.corpus_file, max_vocab_size=int(config.max_vocab_size),
                            max_corpus_size=int(config.max_corpus_size), fw_subsampling_th=config.fw_subsampling_th)
    corpus, idx2word, word2idx, vocab, word_count, word_freq = textloader.load_corpus()
    for data, filename in zip([corpus, word_count, word_freq, vocab, idx2word, word2idx],
                              ['corpus', 'word_count', 'word_freq', 'vocab', 'idx2word', 'word2idx']):
        with open(os.path.join('data', f'{filename}.dat'), 'wb') as f:
            pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
    print("\nTraining for {} epochs...".format(config.epochs))
skipgram = SkipGram(vocab_size=len(idx2word), embedding_dims=config.embedding_dims,
                    neg_samples=config.neg_samples, word_freq=word_freq, padding_idx=word2idx[pad_word])
device = 'cuda' if torch.cuda.is_available() else 'cpu'
skipgram = skipgram.to(device=device)
optim = Adam(skipgram.parameters())
if config.cont_training:
    skipgram.load_state_dict(torch.load(os.path.join('model', 'model.pt')))
    optim.load_state_dict(torch.load(os.path.join('model', 'optimizer.pt')))
dataset = SkipGramData(corpus, word2idx, window=config.window_size)
dataloader = DataLoader(dataset, batch_size=config.mini_batch_size, shuffle=True)
for epoch in range(1, config.epochs + 1):
    pbar = tqdm(dataloader)
    pbar.set_description("[Epoch {}]".format(epoch))
    for targets, contexts in pbar:
        loss = skipgram(targets.to(dtype=torch.long, device=device), contexts.to(dtype=torch.long, device=device))
        optim.zero_grad()
        loss.backward()
        optim.step()
        pbar.set_postfix(loss=loss.item())
    torch.save(skipgram.state_dict(), os.path.join('model', 'model.pt'))
    torch.save(optim.state_dict(), os.path.join('model', 'optimizer.pt'))
    input_idx2vec = skipgram.input_embedding.weight.data.cpu().numpy()
    output_idx2vec = skipgram.output_embedding.weight.data.cpu().numpy()
    write_embedding(os.path.join('embeddings', 'input_embeddings.txt'), idx2word, word2idx, input_idx2vec)
    write_embedding(os.path.join('embeddings', 'output_embeddings.txt'), idx2word, word2idx, output_idx2vec)