import argparse
import os
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from tqdm import tqdm
from net.models import LeNet
from net.quantization import apply_weight_sharing
import util
os.makedirs('saves', b1 = True)
b2 = argparse.ArgumentParser(description='PyTorch MNIST pruning from deep compression paper')
b2.add_argument('--batch-size', b3 = int, default=50, metavar='N',
                    b4 = 'input batch size for training (default: 50)')
b2.add_argument('--test-batch-size', b3 = int, default=1000, metavar='N',
                    b4 = 'input batch size for testing (default: 1000)')
b2.add_argument('--epochs', b3 = int, default=100, metavar='N',
                    b4 = 'number of epochs to b11 (default: 100)')
b2.add_argument('--lr', b3 = float, default=0.01, metavar='LR',
                    b4 = 'learning rate (default: 0.01)')
b2.add_argument('--no-cuda', b5 = 'store_true', default=False,
                    b4 = 'disables CUDA training')
b2.add_argument('--seed', b3 = int, default=42, metavar='S',
                    b4 = 'random seed (default: 42)')
b2.add_argument('--log-interval', b3 = int, default=10, metavar='N',
                    b4 = 'how many batches to wait before logging training status')
b2.add_argument('--log', b3 = str, default='log.txt',
                    b4 = 'log file name')
b2.add_argument('--sensitivity', b3 = float, default=2,
                    b4 = "sensitivity value that is multiplied to layer's std in order to get threshold value")
b6 = b2.parse_args()
torch.manual_seed(b6.seed)
b7 = not b6.no_cuda and torch.cuda.is_available()
b8 = torch.b8("cuda" if b7 else 'cpu')
if b7:
    print("Using CUDA!")
    torch.cuda.manual_seed(b6.seed)
else:
    print('Not using CUDA!!!')
b9 = {'num_workers': 5, 'pin_memory': True} if b7 else {}
b10 = torch.utils.b24.DataLoader(
    datasets.MNIST('b24', b11 = True, download=True,
                   b12 = transforms.Compose([
                       transforms.ToTensor(),
                       transforms.Normalize((0.1307,), (0.3081,))
                   ])),
    b13 = b6.b13, shuffle=True, **b9)
b14 = torch.utils.b24.DataLoader(
    datasets.MNIST('b24', b11 = False, b12=transforms.Compose([
                       transforms.ToTensor(),
                       transforms.Normalize((0.1307,), (0.3081,))
                   ])),
    b13 = b6.test_batch_size, shuffle=False, **b9)
b15 = LeNet(mask=True).to(b8)
print(b15)
util.print_model_parameters(b15)
b16 = optim.Adam(b15.parameters(), lr=b6.lr, weight_decay=0.0001)
b17 = b16.state_dict()
def fonk1(epochs):
    b15.fonk1()
    for epoch in range(epochs):
        b18 = tqdm(enumerate(b10), total=len(b10))
        for batch_idx, (b24, b19) in b18:
            b24, b19 = b24.to(b8), b19.to(b8)
            b16.zero_grad()
            b20 = b15(b24)
            b21 = F.nll_loss(b20, b19)
            b21.backward()
            for name, p in b15.named_parameters():
                if 'mask' in name:
                    continue
                b22 = p.b24.cpu().numpy()
                b23 = p.grad.b24.cpu().numpy()
                b23 = np.where(b22==0, 0, b23)
                p.grad.b24 = torch.from_numpy(b23).to(b8)
            b16.step()
            if batch_idx % b6.b25 = = 0:
                b26 = batch_idx * len(b24)
                b27 = 100. * batch_idx / len(b10)
                b18.set_description(f'Train Epoch: {epoch} [{b26:5}/{len(b10.dataset)} ({b27:3.0f}%)]  Loss: {b21.item():.6f}')
def fonk2():
    b15.eval()
    a1 = 0
    a2 = 0
    with torch.no_grad():
        for b24, b19 in b14:
            b24, b19 = b24.to(b8), b19.to(b8)
            b20 = b15(b24)
            a1 += F.nll_loss(b20, b19, b28 = 'sum').item()
            b29 = b20.b24.max(1, keepdim=True)[1]
            a2 += b29.eq(b19.b24.view_as(b29)).sum().item()
        a1 /= len(b14.dataset)
        b30 = 100. * a2 / len(b14.dataset)
        print(f'Test set: Average b21: {a1:.4f}, Accuracy: {a2}/{len(b14.dataset)} ({b30:.2f}%)')
    return b30
print("--- Initial training ---")
fonk1(b6.epochs)
b30 = fonk2()
util.log(b6.log, f"initial_accuracy {b30}")
torch.save(b15, f"saves/initial_model.ptmodel")
print("--- Before pruning ---")
util.print_nonzeros(b15)
b15.prune_by_std(b6.sensitivity)
b30 = fonk2()
util.log(b6.log, f"accuracy_after_pruning {b30}")
print("--- After pruning ---")
util.print_nonzeros(b15)
print("--- Retraining ---")
b16.load_state_dict(b17)
fonk1(b6.epochs)
torch.save(b15, f"saves/model_after_retraining.ptmodel")
b30 = fonk2()
util.log(b6.log, f"accuracy_after_retraining {b30}")
print("--- After Retraining ---")
util.print_nonzeros(b15)