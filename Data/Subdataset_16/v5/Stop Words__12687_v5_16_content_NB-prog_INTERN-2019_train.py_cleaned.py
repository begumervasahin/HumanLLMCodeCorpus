import os
import pickle
import torch
from torch.optim import Adam
from torch.utils.data import DataLoader
from tqdm import tqdm
from DataHandler import pad_word, TextLoader, SkipGramData, write_embedding
from Model import SkipGram
import config
def fonk1(dirs):
    for directory in dirs:
        os.makedirs(directory, b1 = True)
def fonk2(data_dir):
    with open(os.path.join(data_dir, 'b2.dat'), 'rb') as f:
        b2 = pickle.load(f)
    with open(os.path.join(data_dir, 'b3.dat'), 'rb') as f:
        b3 = pickle.load(f)
    with open(os.path.join(data_dir, 'b4.dat'), 'rb') as f:
        b4 = pickle.load(f)
    with open(os.path.join(data_dir, 'b5.dat'), 'rb') as f:
        b5 = pickle.load(f)
    with open(os.path.join(data_dir, 'b6.dat'), 'rb') as f:
        b6 = pickle.load(f)
    with open(os.path.join(data_dir, 'b7.dat'), 'rb') as f:
        b7 = pickle.load(f)
    return b2, b3, b4, b5, b6, b7
def fonk3(data_dir, state_dict):
    for name, data in state_dict.items():
        with open(os.path.join(data_dir, f'{name}.dat'), 'wb') as f:
            pickle.dump(data, f, b8 = pickle.HIGHEST_PROTOCOL)
def fonk4():
    b9 = TextLoader(
        b10 = config.b10,
        b11 = int(config.b11),
        b12 = int(config.b12),
        b13 = config.b13
    )
    return b9.load_corpus()
def fonk5(b2, b7):
    b14 = SkipGramData(b2, b7, window=config.window_size)
    return DataLoader(b14, b15 = config.mini_batch_size, shuffle=True)
def fonk6(embeddings_dir, b18, b6, b7):
    b16 = b18.input_embedding.weight.data.cpu().numpy()
    b17 = b18.output_embedding.weight.data.cpu().numpy()
    write_embedding(os.path.join(embeddings_dir, 'b16.txt'), b6, b7, b16)
    write_embedding(os.path.join(embeddings_dir, 'b17.txt'), b6, b7, b17)
def fonk7():
    fonk1(['model', 'embeddings', 'data'])
    if config.cont_training:
        b2, b3, b4, b5, b6, b7 = fonk2('data')
        print(f"\nContinuing training from previous state for {config.epochs} epochs ...")
    else:
        b2, b6, b7, b5, b3, b4 = fonk4()
        fonk3('data', {
            'b2': b2,
            'b3': b3,
            'b4': b4,
            'b5': b5,
            'b6': b6,
            'b7': b7
        })
        print(f"\nTraining for {config.epochs} epochs ...")
    b18 = SkipGram(
        b19 = len(b6),
        b20 = config.b20,
        b21 = config.b21,
        b4 = b4,
        b22 = b7[pad_word]
    )
    b23 = 'cuda' if torch.cuda.is_available() else 'cpu'
    b18.to(b23 = b23)
    b24 = Adam(b18.parameters())
    if config.cont_training:
        b18.load_state_dict(torch.load(os.path.join('model', 'model.pt')))
        b24.load_state_dict(torch.load(os.path.join('model', 'b24.pt')))
    b25 = fonk5(b2, b7)
    for epoch in range(1, config.epochs + 1):
        b26 = tqdm(b25, desc=f"[Epoch {epoch}]")
        for b27, b28 in b26:
            b27 = b27.to(dtype=torch.long, b23=b23)
            b28 = b28.to(dtype=torch.long, b23=b23)
            b29 = b18(b27, b28)
            b24.zero_grad()
            b29.backward()
            b24.step()
            b26.set_postfix(b29 = b29.item())
        torch.save(b18.state_dict(), os.path.join('model', 'model.pt'))
        torch.save(b24.state_dict(), os.path.join('model', 'b24.pt'))
        fonk6('embeddings', b18, b6, b7)
if b30 = = "__main__":
    fonk7()