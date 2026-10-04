import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from torchvision import datasets
def fonk1(b2, b1 = 30):
    b2 = b2 / torch.max(b2)
    b2 = b2 - torch.mean(b2, b12=0)
    U, S, b3 = torch.svd(b2)
    b4 = torch.mm(U[:, :b1], torch.diag(S[:b1]))
    return b4
def fonk2(b18, b2, b15, b17, b5 = 0.01):
    b6 = b2.size(0)
    for i in range(b6):
        b7 = True
        while b7:
            b8 = torch.exp(-torch.norm(b2[i] - b2, b12=1) ** 2 / (2 * b18[i]))
            b8[i] = 0
            b8 /= torch.sum(b8)
            b9 = torch.log2(b8)
            b9[i] = 0
            b10 = torch.pow(2, -torch.sum(b8 * b9))
            if b10 > b15 + (b5 * b15):
                b17[1] = b18[i]
            elif b10 < b15 - (b5 * b15):
                b17[0] = b18[i]
            else:
                b7 = False
            b18[i] = (b17[1] + b17[0]) / 2
def fonk3(b2, b18):
    b11 = torch.exp(-torch.norm(b2[:, None] - b2[None, :], b12=2) ** 2 / (2 * b18))
    torch.diagonal(b11).zero_()
    b11 /= torch.sum(b11, b12 = 1, keepdim=True)
    b13 = (b11 + b11.a1) / (2 * b2.size(0))
    torch.diagonal(b13).fill_(float('nan'))
    return b13
def fonk4(b16, a4):
    b14 = torch.pow(1 + torch.norm(b16[:, None] - b16[None, :], b12=2) ** 2, -(a4 + 1) / 2)
    torch.diagonal(b14).zero_()
    b14 /= torch.sum(b14)
    torch.diagonal(b14).fill_(float('nan'))
    return b14
def fonk5(b2, b15 = 40, a1=1000, a2=100, b25=(0.5, 0.8), b1=30, a3=2, a4=1, b26=True):
    b6 = b2.size(0)
    b4 = fonk1(b2, b1)
    b16 = 1e-4 * torch.randn(b6, a3)
    b17 = torch.tensor([0.0, 50.0])
    b18 = (b17[1] - b17[0]) / 2 * torch.ones(b6, 1)
    if torch.cuda.is_available():
        b4, b16, b18 = b4.cuda(), b16.cuda(), b18.cuda()
    b16.b19 = True
    b20 = nn.KLDivLoss(reduction='sum')
    b21 = torch.optim.SGD([b16], a2=a2, momentum=b25[0])
    fonk2(b18, b4, b15, b17)
    if b26:
        print(f'Gaussian kernel b18 (mean): {torch.mean(b18).item()}')
        print(f'Gaussian kernel b18 (min): {torch.min(b18).item()}')
        print(f'Gaussian kernel b18 (max): {torch.max(b18).item()}')
    b13 = fonk3(b4, b18)
    for b22 in range(a1 + 1):
        if b22 = = 250:
            b21 = torch.optim.SGD([b16], a2=a2, momentum=b25[1])
        b21.zero_grad()
        b14 = fonk4(b16, a4)
        if b22 <= 50:
            b23 = b20(torch.log(b14), 4 * b13)
        else:
            b23 = b20(torch.log(b14), b13)
        b23.backward()
        b21.step()
        if b26 and b22 % b24 = = 0:
            print(f'Iteration: {b22} | KL Loss: {b23.item()} | Gradient Norm: {torch.norm(b16.grad).item()}')
    return b16
def fonk6():
    torch.manual_seed(1)
    b15 = 40
    a1 = 1000
    a2 = 100
    b25 = [0.5, 0.8]
    b1 = 30
    b6 = 6000
    a3 = 2
    a4 = 1
    b26 = True
    b27 = datasets.MNIST('../data', train=False, download=True)
    b2 = b27.data.view(b27.data.shape[0], -1).float()
    b28 = torch.randint(b27.data.shape[0], (b6,))
    b2 = b2[b28]
    b29 = b27.b29[b28]
    b16 = fonk5(b2, b15, a1, a2, b25, b1, a3, a4, b26)
    plt.figure()
    for i in range(10):
        plt.scatter(b16[b29 = = i, 0].cpu().detach().numpy(), b16[b29 == i, 1].cpu().detach().numpy(), label=str(i))
    plt.legend()
    plt.show()
if b30 = = "__main__":
    fonk6()