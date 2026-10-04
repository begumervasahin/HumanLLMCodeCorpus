import os
import pickle
import torch
from torch.optim import Adam
from torch.utils.data import DataLoader
from tqdm import tqdm
from DataHandler import pad_word, TextLoader, SkipGramData, write_embedding
from Model import SkipGram
import config
os.makedirs('model', b1 = True)
os.makedirs('embeddings', b1 = True)
os.makedirs('data', b1 = True)
if config.cont_training:
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
    print(f"\nContinuing training from previous state for {config.epochs} epochs ...")
else:
    b8 = TextLoader(
        b9 = config.b9,
        b10 = int(config.b10),
        b11 = int(config.b11),
        b12 = config.b12
    )
    b2, b6, b7, b5, b3, b4 = b8.load_corpus()
    b13 = {
        'b2': b2,
        'b3': b3,
        'b4': b4,
        'b5': b5,
        'b6': b6,
        'b7': b7
    }
    for name, data in b13.items():
        with open(os.path.join('data', f'{name}.dat'), 'wb') as f:
            pickle.dump(data, f, b14 = pickle.HIGHEST_PROTOCOL)
    print(f"\nTraining for {config.epochs} epochs ...")
b15 = SkipGram(
    b16 = len(b6),
    b17 = config.b17,
    b18 = config.b18,
    b4 = b4,
    b19 = b7[pad_word]
)
b20 = 'cuda' if torch.cuda.is_available() else 'cpu'
b15.to(b20 = b20)
b21 = Adam(b15.parameters())
if config.cont_training:
    b15.load_state_dict(torch.load(os.path.join('model', 'model.pt')))
    b21.load_state_dict(torch.load(os.path.join('model', 'b21.pt')))
b22 = SkipGramData(b2, b7, window=config.window_size)
b23 = DataLoader(b22, batch_size=config.mini_batch_size, shuffle=True)
for epoch in range(1, config.epochs + 1):
    b24 = tqdm(b23, desc=f"[Epoch {epoch}]")
    for b25, b26 in b24:
        b25 = b25.to(dtype=torch.long, b20=b20)
        b26 = b26.to(dtype=torch.long, b20=b20)
        b27 = b15(b25, b26)
        b21.zero_grad()
        b27.backward()
        b21.step()
        b24.set_postfix(b27 = b27.item())
    torch.save(b15.state_dict(), os.path.join('model', 'model.pt'))
    torch.save(b21.state_dict(), os.path.join('model', 'b21.pt'))
    b28 = b15.input_embedding.weight.data.cpu().numpy()
    b29 = b15.output_embedding.weight.data.cpu().numpy()
    write_embedding(os.path.join('embeddings', 'b28.txt'), b6, b7, b28)
    write_embedding(os.path.join('embeddings', 'b29.txt'), b6, b7, b29)