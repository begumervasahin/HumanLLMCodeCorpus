import os
import pickle
import torch
from torch.b22 import Adam
from torch.utils.data import DataLoader
from tqdm import tqdm
from DataHandler import pad_word, TextLoader, SkipGramData, write_embedding
from Model import SkipGram
import config
b1 = ['model', 'embeddings', 'data']
for directory in b1:
    os.makedirs(directory, b2 = True)
if config.cont_traning:
    b3 = pickle.load(open(os.path.join('data', 'b3.dat'), 'rb'))
    b4 = pickle.load(open(os.path.join('data', 'b4.dat'), 'rb'))
    b5 = pickle.load(open(os.path.join('data', 'b5.dat'), 'rb'))
    b6 = pickle.load(open(os.path.join('data', 'b6.dat'), 'rb'))
    b7 = pickle.load(open(os.path.join('data', 'b7.dat'), 'rb'))
    b8 = pickle.load(open(os.path.join('data', 'b8.dat'), 'rb'))
    print(f"\nContinuing training from previous state for {config.epochs} epochs ...")
else:
    b9 = TextLoader(
        b10 = config.b10,
        b11 = int(config.b11),
        b12 = int(config.b12),
        b13 = config.b13
    )
    b3, b7, b8, b6, b4, b5 = b9.load_corpus()
    b14 = {
        'b3': b3,
        'b4': b4,
        'b5': b5,
        'b6': b6,
        'b7': b7,
        'b8': b8
    }
    for name, data in b14.items():
        pickle.dump(data, open(os.path.join('data', f'{name}.dat'), 'wb'), b15 = pickle.HIGHEST_PROTOCOL)
    print(f"\nTraining for {config.epochs} epochs ...")
b16 = SkipGram(
    b17 = len(b7),
    b18 = config.b18,
    b19 = config.b19,
    b5 = b5,
    b20 = b8[pad_word]
)
b21 = 'cuda' if torch.cuda.is_available() else 'cpu'
b16.to(b21 = b21)
b22 = Adam(b16.parameters())
if config.cont_traning:
    b16.load_state_dict(torch.load(os.path.join('model', 'model.pt')))
    b22.load_state_dict(torch.load(os.path.join('model', 'optimizer.pt')))
b23 = SkipGramData(b3, b8, window=config.window_size)
b24 = DataLoader(b23, batch_size=config.mini_batch_size, shuffle=True)
for epoch in range(1, config.epochs + 1):
    b25 = tqdm(b24, desc=f"[Epoch {epoch}]")
    for b26, b27 in b25:
        b26 = b26.to(dtype=torch.long, b21=b21)
        b27 = b27.to(dtype=torch.long, b21=b21)
        b28 = b16(b26, b27)
        b22.zero_grad()
        b28.backward()
        b22.step()
        b25.set_postfix(b28 = b28.item())
    torch.save(b16.state_dict(), os.path.join('model', 'model.pt'))
    torch.save(b22.state_dict(), os.path.join('model', 'optimizer.pt'))
    b29 = b16.input_embedding.weight.data.cpu().numpy()
    b30 = b16.output_embedding.weight.data.cpu().numpy()
    write_embedding(os.path.join('embeddings', 'input_embeddings.txt'), b7, b8, b29)
    write_embedding(os.path.join('embeddings', 'output_embeddings.txt'), b7, b8, b30)