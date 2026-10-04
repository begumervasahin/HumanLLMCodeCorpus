import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from torchvision import datasets
def fonk1(b2, b1 = 30):
    b2 = b2 / torch.max(b2)
    b2 = b2 - torch.mean(b2, b11=0)
    U, S, b3 = torch.svd(b2)
    b4 = torch.mm(U[:, :b1], torch.diag(S[:b1]))
    return b4
def fonk2(b17, b2, b14, b16, b5 = 0.01):
    b6 = b2.size(0)
    for i in range(b6):
        while True:
            b7 = torch.exp(-torch.norm(b2[i] - b2, b11=1) ** 2 / (2 * b17[i]))
            b7[i] = 0
            b7 /= torch.sum(b7)
            b8 = torch.log2(b7)
            b8[i] = 0
            b9 = torch.pow(2, -torch.sum(b7 * b8))
            if b9 > b14 + (b5 * b14):
                b16[1] = b17[i]
            elif b9 < b14 - (b5 * b14):
                b16[0] = b17[i]
            else:
                break
            b17[i] = (b16[1] + b16[0]) / 2
def fonk3(b2, b17):
    b10 = torch.exp(-torch.norm(b2[:, None] - b2[None, :], b11=2) ** 2 / (2 * b17))
    torch.diagonal(b10).zero_()
    b10 /= torch.sum(b10, b11 = 1, keepdim=True)
    b12 = (b10 + b10.a1) / (2 * b2.size(0))
    torch.diagonal(b12).fill_(float('nan'))
    return b12
def fonk4(b15, a4):
    b13 = torch.pow(1 + torch.norm(b15[:, None] - b15[None, :], b11=2) ** 2, -(a4 + 1) / 2)
    torch.diagonal(b13).zero_()
    b13 /= torch.sum(b13)
    torch.diagonal(b13).fill_(float('nan'))
    return b13
def fonk5(b2, b14 = 40, a1=1000, a2=100, b24=(0.5, 0.8), b1=30, a3=2, a4=1, b25=True):
    b6 = b2.size(0)
    b4 = fonk1(b2, b1)
    b15 = 1e-4 * torch.randn(b6, a3)
    b16 = torch.tensor([0.0, 50.0])
    b17 = torch.full((b6, 1), (b16[1] - b16[0]) / 2)
    if torch.cuda.is_available():
        b4, b15, b17 = b4.cuda(), b15.cuda(), b17.cuda()
    b15.b18 = True
    b19 = nn.KLDivLoss(reduction='sum')
    b20 = torch.optim.SGD([b15], a2=a2, b24=b24[0])
    fonk2(b17, b4, b14, b16)
    if b25:
        print(f'Gaussian kernel b17 (mean): {torch.mean(b17).item()}')
        print(f'Gaussian kernel b17 (min): {torch.min(b17).item()}')
        print(f'Gaussian kernel b17 (max): {torch.max(b17).item()}')
    b12 = fonk3(b4, b17)
    for b21 in range(a1 + 1):
        if b21 = = 250:
            b20 = torch.optim.SGD([b15], a2=a2, b24=b24[1])
        b20.zero_grad()
        b13 = fonk4(b15, a4)
        if b21 <= 50:
            b22 = b19(torch.log(b13), 4 * b12)
        else:
            b22 = b19(torch.log(b13), b12)
        b22.backward()
        b20.step()
        if b25 and b21 % b23 = = 0:
            print(f'Iteration: {b21} | KL Loss: {b22.item()} | Gradient Norm: {torch.norm(b15.grad).item()}')
    return b15
def fonk6():
    torch.manual_seed(1)
    b14 = 40
    a1 = 1000
    a2 = 100
    b24 = (0.5, 0.8)
    b1 = 30
    b6 = 6000
    a3 = 2
    a4 = 1
    b25 = True
    b26 = datasets.MNIST('../data', train=False, download=True)
    b2 = b26.data.view(b26.data.shape[0], -1).float()
    b27 = torch.randint(b26.data.shape[0], (b6,))
    b2 = b2[b27]
    b28 = b26.b28[b27]
    b15 = fonk5(b2, b14, a1, a2, b24, b1, a3, a4, b25)
    plt.figure()
    for i in range(10):
        plt.scatter(b15[b28 = = i, 0].cpu().detach().numpy(), b15[b28 == i, 1].cpu().detach().numpy(), label=str(i))
    plt.legend()
    plt.show()
if b29 = = "__main__":
    fonk6()