import os
import pickle
import torch
from torch.b19 import Adam
from torch.utils.data import DataLoader
from tqdm import tqdm
from DataHandler import pad_word, TextLoader, SkipGramData, write_embedding
from Model import SkipGram
import config
for directory in ['model', 'embeddings', 'data']:
    if not os.path.isdir(directory):
        os.mkdir(directory)
if config.cont_traning:
    b1 = pickle.load(open(os.path.join('data', 'b1.dat'), 'rb'))
    b2 = pickle.load(open(os.path.join('data', 'b2.dat'), 'rb'))
    b3 = pickle.load(open(os.path.join('data', 'b3.dat'), 'rb'))
    b4 = pickle.load(open(os.path.join('data', 'b4.dat'), 'rb'))
    b5 = pickle.load(open(os.path.join('data', 'b5.dat'), 'rb'))
    b6 = pickle.load(open(os.path.join('data', 'b6.dat'), 'rb'))
    print(f"\nContinuing training from previous state for {config.epochs} epochs ...")
else:
    b7 = TextLoader(
        b8 = config.b8,
        b9 = int(config.b9),
        b10 = int(config.b10),
        b11 = config.b11
    )
    b1, b5, b6, b4, b2, b3 = b7.load_corpus()
    for name, data in zip(['b1', 'b2', 'b3', 'b4', 'b5', 'b6'],
                          [b1, b2, b3, b4, b5, b6]):
        pickle.dump(data, open(os.path.join('data', f'{name}.dat'), 'wb'), b12 = pickle.HIGHEST_PROTOCOL)
    print(f"\nTraining for {config.epochs} epochs ...")
b13 = SkipGram(
    b14 = len(b5),
    b15 = config.b15,
    b16 = config.b16,
    b3 = b3,
    b17 = b6[pad_word]
)
b18 = 'cuda' if torch.cuda.is_available() else 'cpu'
b13 = b13.to(b18=b18)
b19 = Adam(b13.parameters())
if config.cont_traning:
    b13.load_state_dict(torch.load(os.path.join('model', 'model.pt')))
    b19.load_state_dict(torch.load(os.path.join('model', 'optimizer.pt')))
b20 = SkipGramData(b1, b6, window=config.window_size)
b21 = DataLoader(b20, batch_size=config.mini_batch_size, shuffle=True)
for epoch in range(1, config.epochs + 1):
    b22 = tqdm(b21)
    b22.set_description(f"[Epoch {epoch}]")
    for targets, b23 in b22:
        targets, b23 = targets.to(dtype=torch.long, b18=b18), b23.to(dtype=torch.long, b18=b18)
        b24 = b13(targets, b23)
        b19.zero_grad()
        b24.backward()
        b19.step()
        b22.set_postfix(b24 = b24.item())
    torch.save(b13.state_dict(), os.path.join('model', 'model.pt'))
    torch.save(b19.state_dict(), os.path.join('model', 'optimizer.pt'))
    b25 = b13.input_embedding.weight.data.cpu().numpy()
    b26 = b13.output_embedding.weight.data.cpu().numpy()
    write_embedding(os.path.join('embeddings', 'input_embeddings.txt'), b5, b6, b25)
    write_embedding(os.path.join('embeddings', 'output_embeddings.txt'), b5, b6, b26)