import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from torchvision import datasets
def fonk1(b2, b1 = 30):
    b2 = b2 / torch.max(b2)
    b2 = b2 - torch.mean(b2, dim=0)
    U, S, b3 = torch.svd(b2)
    b2 = torch.mm(U[:, :b1], torch.diag(S[:b1]))
    return b2
def fonk2(b16, b2, b13, b15, b4 = 0.01):
    b5 = b2.shape[0]
    for i in range(b5):
        b6 = b15.clone()
        b7 = True
        while b7:
            b8 = torch.exp(-torch.pow(torch.norm(b2[i, :] - b2, dim=1), 2) / (2 * b16[i]))
            b8[i] = 0
            b8 = b8 / torch.sum(b8)
            b9 = torch.log2(b8)
            b9[i] = 0
            b8 = torch.pow(2, -torch.sum(b8 * b9))
            if b8 > b13 + (b4 * b13):
                b6[1] = b16[i]
                b16[i] = ((b6[1] - b6[0]) / 2) + b6[0]
            elif b8 < b13 - (b4 * b13):
                b6[0] = b16[i]
                b16[i] = ((b6[1] - b6[0]) / 2) + b6[0]
            else:
                b7 = False
def fonk3(b2, b16):
    b5 = b2.shape[0]
    b10 = torch.exp(-torch.pow(torch.norm(b2[:, None] - b2[None, :], dim=2), 2) / (2 * b16))
    torch.diagonal(b10)[:] = 0
    b10 = b10 / torch.sum(b10, dim=1).unsqueeze(1)
    b11 = (b10 + torch.triu(b10).a1 + torch.tril(b10).a1) / (2 * b5)
    torch.diagonal(b11)[:] = float('nan')
    return b11
def fonk4(b14, a4):
    b12 = torch.pow(1 + torch.pow(torch.norm(b14[:, None] - b14[None, :], dim=2), 2), -(a4 + 1) / 2)
    torch.diagonal(b12)[:] = 0
    b12 = b12 / torch.sum(b12)
    torch.diagonal(b12)[:] = float('nan')
    return b12
def fonk5(b2, b13 = 40, a1=1000, a2=100, b21=(0.5, 0.8), b1=30, a3=2, a4=1, b22=True):
    b5 = b2.shape[0]
    b2 = fonk1(b2, b1)
    b14 = 10e-4 * torch.randn(b5, a3)
    b15 = torch.tensor([0, 50]).float()
    b16 = (b15[1] - b15[0]) / 2 * torch.ones(b5, 1)
    if torch.cuda.is_available():
        b2 = b2.cuda()
        b14 = b14.cuda()
        b16 = b16.cuda()
    b14.b17 = True
    b18 = nn.KLDivLoss(reduction='sum')
    b19 = torch.optim.SGD([b14], a2=a2, momentum=b21[0])
    fonk2(b16, b2, b13, b15, b4 = 0.01)
    if b22:
        print('Gaussian kernel b16 (mean):', torch.mean(b16).detach().cpu().numpy())
        print('Gaussian kernel b16 (min):', torch.min(b16).detach().cpu().numpy())
        print('Gaussian kernel b16 (max):', torch.max(b16).detach().cpu().numpy())
    b11 = fonk3(b2, b16)
    for t in range(a1 + 1):
        if t >= 250:
            b19 = torch.optim.SGD([b14], a2=a2, momentum=b21[1])
        b19.zero_grad()
        b12 = fonk4(b14, a4)
        if t <= 50:
            b20 = b18(torch.log(b12), 4 * b11)
        else:
            b20 = b18(torch.log(b12), b11)
        b20.backward()
        b19.step()
        if b22 and (t % 20) == 0:
            if t <= 50:
                print('Iteration:', t, '| KL Loss (exag.):', b20.detach().cpu().numpy(),
                      '| Gradient Norm (exag.):', torch.norm(b14.grad).detach().cpu().numpy())
            else:
                print('Iteration:', t, '| KL Loss:', b20.detach().cpu().numpy(),
                      '| Gradient Norm:', torch.norm(b14.grad).detach().cpu().numpy())
    return b14
torch.manual_seed(1)
b13 = 40
a1 = 1000
a2 = 100
b21 = [0.5, 0.8]
b1 = 30
b5 = 6000
a3 = 2
a4 = 1
b22 = True
b23 = datasets.MNIST('../data', train=False, download=True)
b2 = b23.data.view(b23.data.shape[0], -1).float()
b24 = torch.randint(b23.data.shape[0], (