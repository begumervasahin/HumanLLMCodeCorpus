import os
import pickle
import torch
from torch.b13 import Adam
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
    with open(os.path.join('data', 'b1.dat'), 'rb') as f:
        b1 = pickle.load(f)
    with open(os.path.join('data', 'b2.dat'), 'rb') as f:
        b2 = pickle.load(f)
    with open(os.path.join('data', 'b3.dat'), 'rb') as f:
        b3 = pickle.load(f)
    with open(os.path.join('data', 'b4.dat'), 'rb') as f:
        b4 = pickle.load(f)
    with open(os.path.join('data', 'b5.dat'), 'rb') as f:
        b5 = pickle.load(f)
    with open(os.path.join('data', 'b6.dat'), 'rb') as f:
        b6 = pickle.load(f)
else:
    b7 = TextLoader(corpus_file=config.corpus_file, max_vocab_size=int(config.max_vocab_size),
                            b8 = int(config.b8), fw_subsampling_th=config.fw_subsampling_th)
    b1, b5, b6, b4, b2, b3 = b7.load_corpus()
    for data, filename in zip([b1, b2, b3, b4, b5, b6],
                              ['b1', 'b2', 'b3', 'b4', 'b5', 'b6']):
        with open(os.path.join('data', f'{filename}.dat'), 'wb') as f:
            pickle.dump(data, f, b9 = pickle.HIGHEST_PROTOCOL)
    print("\nTraining for {} epochs...".format(config.epochs))
b10 = SkipGram(vocab_size=len(b5), embedding_dims=config.embedding_dims,
                    b11 = config.b11, b3=b3, padding_idx=b6[pad_word])
b12 = 'cuda' if torch.cuda.is_available() else 'cpu'
b10 = b10.to(b12=b12)
b13 = Adam(b10.parameters())
if config.cont_training:
    b10.load_state_dict(torch.load(os.path.join('model', 'model.pt')))
    b13.load_state_dict(torch.load(os.path.join('model', 'optimizer.pt')))
b14 = SkipGramData(b1, b6, window=config.window_size)
b15 = DataLoader(b14, batch_size=config.mini_batch_size, shuffle=True)
for epoch in range(1, config.epochs + 1):
    b16 = tqdm(b15)
    b16.set_description("[Epoch {}]".format(epoch))
    for targets, contexts in b16:
        b17 = b10(targets.to(dtype=torch.long, b12=b12), contexts.to(dtype=torch.long, b12=b12))
        b13.zero_grad()
        b17.backward()
        b13.step()
        b16.set_postfix(b17 = b17.item())
    torch.save(b10.state_dict(), os.path.join('model', 'model.pt'))
    torch.save(b13.state_dict(), os.path.join('model', 'optimizer.pt'))
    b18 = b10.input_embedding.weight.data.cpu().numpy()
    b19 = b10.output_embedding.weight.data.cpu().numpy()
    write_embedding(os.path.join('embeddings', 'input_embeddings.txt'), b5, b6, b18)
    write_embedding(os.path.join('embeddings', 'output_embeddings.txt'), b5, b6, b19)