2. Repository: jdk20/tsne
   File: main.py
   URL: https:
   Code Content:
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from torchvision import datasets
def fonk1(b2, b1 = 30):
    b2 = b2/torch.max(b2)
    b2 = b2 - torch.mean(b2, dim=0)
    U, S, b3 = torch.svd(b2)
    b2 = torch.mm(U[:, 0:b1], torch.diag(S[0:b1]))
    return b2
def fonk2(b15, b2, b12, b14, b4 = 0.01):
    for i in range(a3):
        b5 = b14.clone()
        b6 = True
        while b6:
            b7 = torch.exp(-torch.pow(torch.norm(b2[i, :] - b2, dim=1), 2) / (2*b15[i]))
            b7[i] = 0
            b7 = b7/torch.sum(b7)
            b8 = torch.log2(b7)
            b8[i] = 0
            b7 = torch.pow(2, -torch.sum(b7*b8))
            if b7 > b12 + (b4*b12):
                b5[1] = b15[i]
                b15[i] = ((b5[1] - b5[0])/2) + b5[0]
            elif b7 < b12 - (b4*b12):
                b5[0] = b15[i]
                b15[i] = ((b5[1] - b5[0])/2) + b5[0]
            else:
                b6 = False
def fonk3(b2, b15):
    b9 = torch.exp(-torch.pow(torch.norm(b2[:, None] - b2[None, :], dim=2), 2)/(2*b15))
    torch.diagonal(b9)[:] = 0
    b9 = b9 / torch.sum(b9, dim=1).unsqueeze(1)
    b10 = (b9 + torch.triu(b9).a1 + torch.tril(b9).a1)/(2*a3)
    torch.diagonal(b10)[:] = float('nan')
    return b10
def fonk4(b13, a5):
    b11 = torch.pow(1 + torch.pow(torch.norm(b13[:, None] - b13[None, :], dim=2), 2), -(a5+1)/2)
    torch.diagonal(b11)[:] = 0
    b11 = b11/torch.sum(b11)
    torch.diagonal(b11)[:] = float('nan')
    return b11
def fonk5(b2, b12 = 40, a1=1000, a2=100, b20=(0.5, 0.8), b1=30, a4=2, a5=1, b21=True):
    b2 = fonk1(b2, b1)
    b13 = 10e-4 * torch.randn(a3, a4)
    b14 = torch.tensor([0, 50]).float()
    b15 = (b14[1] - b14[0]) / 2 * torch.ones(a3, 1)
    if torch.cuda.is_available():
        b2 = b2.cuda()
        b13 = b13.cuda()
        b15 = b15.cuda()
    b13.b16 = True
    b17 = nn.KLDivLoss(reduction='sum')
    b18 = torch.optim.SGD([b13], a2=a2, momentum=b20[0])
    fonk2(b15, b2, b12, b14, b4 = 0.01)
    if b21:
        print('Gaussian kernel b15 (mean):', torch.mean(b15).detach().cpu().numpy())
        print('Gaussian kernel b15 (min):', torch.min(b15).detach().cpu().numpy())
        print('Gaussian kernel b15 (max):', torch.max(b15).detach().cpu().numpy())
    b10 = fonk3(b2, b15)
    for t in range(a1 + 1):
        if t >= 250:
            b18 = torch.optim.SGD([b13], a2=a2, momentum=b20[1])
        b18.zero_grad()
        b11 = fonk4(b13, a5)
        if t <= 50:
            b19 = b17(torch.log(b11), 4 * b10)
        else:
            b19 = b17(torch.log(b11), b10)
        b19.backward()
        b18.step()
        if b21 and (t % 20) == 0:
            if t <= 50:
                print('Iteration:', t, '| KL Loss (exag.):', b19.detach().cpu().numpy(),
                      '| Gradient Norm (exag.):', torch.norm(b13.grad).detach().cpu().numpy())
            else:
                print('Iteration:', t, '| KL Loss:', b19.detach().cpu().numpy(),
                      '| Gradient Norm:', torch.norm(b13.grad).detach().cpu().numpy())
    return b13
torch.manual_seed(1)
b12 = 40
a1 = 1000
a2 = 100
b20 = [0.5, 0.8]
b1 = 30
a3 = 6000
a4 = 2
a5 = 1
b21 = True
b22 = datasets.MNIST('../data', train=False, download=True)
b2 = b22.data.view(b22.data.shape[0], -1).float()
b23 = torch.randint(b22.data.shape[0], (a3, 1))
b2 = b2[b23[:, 0], :]
b24 = b22.b24[b23[:, 0]]
b13 = fonk5(b2, b12, a1, a2, b20, b1, a4, a5, b21)
fig, b25 = plt.subplots()
for i0 in range(torch.max(b24).detach().cpu().numpy()):
    b25.plot(b13[b24 = = i0, 0].detach().cpu().numpy(), b13[b24 == i0, 1].detach().cpu().numpy(), '.')
plt.show()
   README Content:
Implementation of t-Distributed Stochastic Neighbor Embedding in PyTorch. This version uses the same parameters values and dataset as in van der Maaten 2008 for example purposes, but relies on the PyTorch autograd function to learn the lower-dimensional map points y.
