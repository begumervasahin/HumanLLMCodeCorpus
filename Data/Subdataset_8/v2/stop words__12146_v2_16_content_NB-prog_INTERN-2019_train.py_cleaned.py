import os
import pickle
import torch
from torch.optim import Adam
from torch.utils.data import DataLoader
from tqdm import tqdm
from DataHandler import pad_word, TextLoader, SkipGramData, write_embedding
from Model import SkipGram
import config
if not os.path.isdir('model'):
    os.mkdir('model')
if not os.path.isdir('embeddings'):
    os.mkdir('embeddings')
if not os.path.isdir('data'):
    os.mkdir('data')
if config.cont_traning:
    corpus = pickle.load(open(os.path.join('data', 'corpus.dat'), 'rb'))
    word_count = pickle.load(open(os.path.join('data', 'word_count.dat'), 'rb'))
    word_freq = pickle.load(open(os.path.join('data', 'word_freq.dat'), 'rb'))
    vocab = pickle.load(open(os.path.join('data', 'vocab.dat'), 'rb'))
    idx2word = pickle.load(open(os.path.join('data', 'idx2word.dat'), 'rb'))
    word2idx = pickle.load(open(os.path.join('data', 'word2idx.dat'), 'rb'))
    print("\nContinuing training from previous state for {} epochs ...".format(config.epochs))
else:
    text_loader = TextLoader(corpus_file=config.corpus_file, max_vocab_size=int(config.max_vocab_size),
                             max_corpus_size=int(config.max_corpus_size), fw_subsampling_th=config.fw_subsampling_th)
    corpus, idx2word, word2idx, vocab, word_count, word_freq = text_loader.load_corpus()
    pickle.dump(corpus, open(os.path.join('data', 'corpus.dat'), 'wb'), protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(word_count, open(os.path.join('data', 'word_count.dat'), 'wb'), protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(word_freq, open(os.path.join('data', 'word_freq.dat'), 'wb'), protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(vocab, open(os.path.join('data', 'vocab.dat'), 'wb'), protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(idx2word, open(os.path.join('data', 'idx2word.dat'), 'wb'), protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(word2idx, open(os.path.join('data', 'word2idx.dat'), 'wb'), protocol=pickle.HIGHEST_PROTOCOL)
    print("\nTraining for {} epochs ...".format(config.epochs))
skipgram_model = SkipGram(vocab_size=len(idx2word), embedding_dims=config.embedding_dims,
                          neg_samples=config.neg_samples, word_freq=word_freq, padding_idx=word2idx[pad_word])
device = 'cuda' if torch.cuda.is_available() else 'cpu'
skipgram_model = skipgram_model.to(device=device)
optimizer = Adam(skipgram_model.parameters())
if config.cont_traning:
    skipgram_model.load_state_dict(torch.load(os.path.join('model', 'model.pt')))
    optimizer.load_state_dict(torch.load(os.path.join('model', 'optimizer.pt')))
dataset = SkipGramData(corpus, word2idx, window=config.window_size)
dataloader = DataLoader(dataset, batch_size=config.mini_batch_size, shuffle=True)
for epoch in range(1, config.epochs + 1):
    progress_bar = tqdm(dataloader)
    progress_bar.set_description("[Epoch {}]".format(epoch))
    for targets, contexts in progress_bar:
        loss = skipgram_model(targets.to(dtype=torch.long, device=device),
                               contexts.to(dtype=torch.long, device=device))
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        progress_bar.set_postfix(loss=loss.item())
    torch.save(skipgram_model.state_dict(), os.path.join('model', 'model.pt'))
    torch.save(optimizer.state_dict(), os.path.join('model', 'optimizer.pt'))
    input_embeddings = skipgram_model.input_embedding.weight.data.cpu().numpy()
    output_embeddings = skipgram_model.output_embedding.weight.data.cpu().numpy()
    write_embedding(os.path.join('embeddings', 'input_embeddings.txt'), idx2word, word2idx, input_embeddings)
    write_embedding(os.path.join('embeddings', 'output_embeddings.txt'), idx2word, word2idx, output_embeddings)