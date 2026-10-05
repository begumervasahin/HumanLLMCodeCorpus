import os
import pickle
import torch
from torch.b14 import Adam
from torch.utils.data import DataLoader
from tqdm import tqdm
from DataHandler import TextLoader, SkipGramData, write_embedding
from Model import SkipGram
import config
b1 = ['model', 'embeddings', 'data']
for directory in b1:
    if not os.path.isdir(directory):
        os.mkdir(directory)
if config.cont_training:
    print("\nContinuing training from the previous state for {} epochs...".format(config.epochs))
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
    with open(os.path.join('data', 'b7.dat'), 'rb') as f:
        b7 = pickle.load(f)
else:
    b8 = TextLoader(corpus_file=config.corpus_file, max_vocab_size=int(config.max_vocab_size),
                             b9 = int(config.b9), fw_subsampling_th=config.fw_subsampling_th)
    b2, b6, b7, b5, b3, b4 = b8.load_corpus()
    for data, filename in zip([b2, b3, b4, b5, b6, b7],
                              ['b2', 'b3', 'b4', 'b5', 'b6', 'b7']):
        with open(os.path.join('data', f'{filename}.dat'), 'wb') as f:
            pickle.dump(data, f, b10 = pickle.HIGHEST_PROTOCOL)
    print("\nTraining for {} epochs...".format(config.epochs))
b11 = SkipGram(vocab_size=len(b6), embedding_dims=config.embedding_dims,
                    b12 = config.b12, b4=b4, padding_idx=b7[pad_word])
b13 = 'cuda' if torch.cuda.is_available() else 'cpu'
b11 = b11.to(b13=b13)
b14 = Adam(b11.parameters())
if config.cont_training:
    b11.load_state_dict(torch.load(os.path.join('model', 'model.pt')))
    b14.load_state_dict(torch.load(os.path.join('model', 'optimizer.pt')))
b15 = SkipGramData(b2, b7, window=config.window_size)
b16 = DataLoader(b15, batch_size=config.mini_batch_size, shuffle=True)
for epoch in range(1, config.epochs + 1):
    b17 = tqdm(b16)
    b17.set_description("[Epoch {}]".format(epoch))
    for targets, contexts in b17:
        b18 = b11(targets.to(dtype=torch.long, b13=b13), contexts.to(dtype=torch.long, b13=b13))
        b14.zero_grad()
        b18.backward()
        b14.step()
        b17.set_postfix(b18 = b18.item())
    torch.save(b11.state_dict(), os.path.join('model', 'model.pt'))
    torch.save(b14.state_dict(), os.path.join('model', 'optimizer.pt'))
    b19 = b11.input_embedding.weight.data.cpu().numpy()
    b20 = b11.output_embedding.weight.data.cpu().numpy()
    write_embedding(os.path.join('embeddings', 'input_embeddings.txt'), b6, b7, b19)
    write_embedding(os.path.join('embeddings', 'output_embeddings.txt'), b6, b7, b20)