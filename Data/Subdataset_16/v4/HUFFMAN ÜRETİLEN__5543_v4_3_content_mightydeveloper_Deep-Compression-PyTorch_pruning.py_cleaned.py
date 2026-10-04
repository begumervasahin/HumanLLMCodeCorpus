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
b2 = argparse.ArgumentParser(description='PyTorch MNIST Pruning based on Deep Compression Paper')
b2.add_argument('--batch-size', b3 = int, default=50, metavar='N', help='Input batch size for training (default: 50)')
b2.add_argument('--test-batch-size', b3 = int, default=1000, metavar='N', help='Input batch size for testing (default: 1000)')
b2.add_argument('--epochs', b3 = int, default=100, metavar='N', help='Number of epochs to b10 (default: 100)')
b2.add_argument('--lr', b3 = float, default=0.01, metavar='LR', help='Learning rate (default: 0.01)')
b2.add_argument('--no-cuda', b4 = 'store_true', default=False, help='Disables CUDA training')
b2.add_argument('--seed', b3 = int, default=42, metavar='S', help='Random seed (default: 42)')
b2.add_argument('--log-interval', b3 = int, default=10, metavar='N', help='Batches to wait before logging training status')
b2.add_argument('--log', b3 = str, default='log.txt', help='Log file name')
b2.add_argument('--sensitivity', b3 = float, default=2, help="Sensitivity value multiplied to layer's std to get threshold value")
b5 = b2.parse_args()
torch.manual_seed(b5.seed)
b6 = not b5.no_cuda and torch.cuda.is_available()
b7 = torch.b7("cuda" if b6 else "cpu")
if b6:
    print("Using CUDA!")
    torch.cuda.manual_seed(b5.seed)
else:
    print("Not using CUDA!")
b8 = {'num_workers': 5, 'pin_memory': True} if b6 else {}
b9 = torch.utils.b23.DataLoader(
    datasets.MNIST('b23', b10 = True, download=True,
                   b11 = transforms.Compose([
                       transforms.ToTensor(),
                       transforms.Normalize((0.1307,), (0.3081,))
                   ])),
    b12 = b5.b12, shuffle=True, **b8)
b13 = torch.utils.b23.DataLoader(
    datasets.MNIST('b23', b10 = False, b11=transforms.Compose([
                       transforms.ToTensor(),
                       transforms.Normalize((0.1307,), (0.3081,))
                   ])),
    b12 = b5.test_batch_size, shuffle=False, **b8)
b14 = LeNet(mask=True).to(b7)
b15 = optim.Adam(b14.parameters(), lr=b5.lr, weight_decay=0.0001)
b16 = b15.state_dict()
def fonk1(epochs):
    b14.fonk1()
    for epoch in range(epochs):
        b17 = tqdm(enumerate(b9), total=len(b9))
        for batch_idx, (b23, b18) in b17:
            b23, b18 = b23.to(b7), b18.to(b7)
            b15.zero_grad()
            b19 = b14(b23)
            b20 = F.nll_loss(b19, b18)
            b20.backward()
            for name, param in b14.named_parameters():
                if 'mask' in name:
                    continue
                b21 = param.b23.cpu().numpy()
                b22 = param.grad.b23.cpu().numpy()
                b22 = np.where(b21 == 0, 0, b22)
                param.grad.b23 = torch.from_numpy(b22).to(b7)
            b15.step()
            if batch_idx % b5.b24 = = 0:
                b17.set_description(f'Train Epoch: {epoch} [{batch_idx * len(b23)}/{len(b9.dataset)} ({100. * batch_idx / len(b9):.0f}%)]  Loss: {b20.item():.6f}')
def fonk2():
    b14.eval()
    a1 = 0
    a2 = 0
    with torch.no_grad():
        for b23, b18 in b13:
            b23, b18 = b23.to(b7), b18.to(b7)
            b19 = b14(b23)
            a1 += F.nll_loss(b19, b18, b25 = 'sum').item()
            b26 = b19.argmax(dim=1, keepdim=True)
            a2 += b26.eq(b18.view_as(b26)).sum().item()
    a1 /= len(b13.dataset)
    b27 = 100. * a2 / len(b13.dataset)
    print(f'Test set: Average b20: {a1:.4f}, Accuracy: {a2}/{len(b13.dataset)} ({b27:.2f}%)')
    return b27
print("--- Initial training ---")
fonk1(b5.epochs)
b28 = fonk2()
util.log(b5.log, f"b28 {b28}")
torch.save(b14.state_dict(), f"saves/initial_model.pt")
print("--- Before pruning ---")
util.print_nonzeros(b14)
b14.prune_by_std(b5.sensitivity)
b29 = fonk2()
util.log(b5.log, f"accuracy_after_pruning {b29}")
print("--- After pruning ---")
util.print_nonzeros(b14)
print("--- Retraining ---")
b15.load_state_dict(b16)
fonk1(b5.epochs)
torch.save(b14.state_dict(), f"saves/model_after_retraining.pt")
b30 = fonk2()
util.log(b5.log, f"accuracy_after_retraining {b30}")
print("--- After Retraining ---")
util.print_nonzeros(b14)