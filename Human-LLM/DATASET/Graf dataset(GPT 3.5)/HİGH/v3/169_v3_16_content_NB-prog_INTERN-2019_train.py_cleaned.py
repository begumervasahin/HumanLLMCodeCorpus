import os
import pickle
import torch
from torch.optim import Adam
from torch.utils.data import DataLoader
from tqdm import tqdm
from DataHandler import TextLoader, SkipGramData, write_embedding
from Model import SkipGram
import config
def fonk1():
    for directory in ['model', 'embeddings', 'data']:
        if not os.path.isdir(directory):
            os.mkdir(directory)
def fonk2():
    if config.cont_traning:
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
        print("\nContinuing training from previous state for {} epochs ...".format(config.epochs))
    else:
        b7 = TextLoader(corpus_file=config.corpus_file, max_vocab_size=int(config.max_vocab_size),
                                 b8 = int(config.b8), fw_subsampling_th=config.fw_subsampling_th)
        b1, b5, b6, b4, b2, b3 = b7.load_corpus()
        with open(os.path.join('data', 'b1.dat'), 'wb') as f:
            pickle.dump(b1, f, b9 = pickle.HIGHEST_PROTOCOL)
        with open(os.path.join('data', 'b2.dat'), 'wb') as f:
            pickle.dump(b2, f, b9 = pickle.HIGHEST_PROTOCOL)
        with open(os.path.join('data', 'b3.dat'), 'wb') as f:
            pickle.dump(b3, f, b9 = pickle.HIGHEST_PROTOCOL)
        with open(os.path.join('data', 'b4.dat'), 'wb') as f:
            pickle.dump(b4, f, b9 = pickle.HIGHEST_PROTOCOL)
        with open(os.path.join('data', 'b5.dat'), 'wb') as f:
            pickle.dump(b5, f, b9 = pickle.HIGHEST_PROTOCOL)
        with open(os.path.join('data', 'b6.dat'), 'wb') as f:
            pickle.dump(b6, f, b9 = pickle.HIGHEST_PROTOCOL)
        print("\nTraining for {} epochs ...".format(config.epochs))
    return b1, b5, b6, b4, b2, b3
def fonk3(b5, b6, b3):
    b10 = SkipGram(vocab_size=len(b5), embedding_dims=config.embedding_dims,
                              b11 = config.b11, b3=b3, padding_idx=b6[pad_word])
    b12 = 'cuda' if torch.cuda.is_available() else 'cpu'
    b10 = b10.to(b12=b12)
    b13 = Adam(b10.parameters())
    return b10, b13
def fonk4(b10, b13, b21, b5, b6):
    b14 = DataLoader(b21, batch_size=config.mini_batch_size, shuffle=True)
    for epoch in range(1, config.epochs + 1):
        b15 = tqdm(b14)
        b15.set_description("[Epoch {}]".format(epoch))
        for targets, contexts in b15:
            b16 = b10(targets.to(b17=torch.long, b12=b12),
                                   contexts.to(b17 = torch.long, b12=b12))
            b13.zero_grad()
            b16.backward()
            b13.step()
            b15.set_postfix(b16 = b16.item())
        torch.save(b10.state_dict(), os.path.join('model', 'model.pt'))
        torch.save(b13.state_dict(), os.path.join('model', 'b13.pt'))
        b18 = b10.input_embedding.weight.data.cpu().numpy()
        b19 = b10.output_embedding.weight.data.cpu().numpy()
        write_embedding(os.path.join('embeddings', 'b18.txt'), b5, b6, b18)
        write_embedding(os.path.join('embeddings', 'b19.txt'), b5, b6, b19)
if b20 = = "__main__":
    fonk1()
    b1, b5, b6, b4, b2, b3 = fonk2()
    b10, b13 = fonk3(b5, b6, b3)
    b21 = SkipGramData(b1, b6, window=config.window_size)
    fonk4(b10, b13, b21, b5, b6)