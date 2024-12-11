import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from torchvision import datasets
def fonk1(b15, b1 = 30):
    b2 = b15 / torch.max(b15)
    b3 = b2 - torch.mean(b2, dim=0)
    U, S, b4 = torch.svd(b3)
    b5 = torch.mm(U[:, :b1], torch.diag(S[:b1]))
    return b5
def fonk2(b18, b15, b14, b17, b6 = 0.01):
    for i in range(b15.shape[0]):
        b7 = b17.clone()
        b8 = True
        while b8:
            b9 = torch.exp(-torch.pow(torch.norm(b15[i, :] - b15, dim=1), 2) / (2 * b18[i]))
            b9[i] = 0
            b9 = b9 / torch.sum(b9)
            b10 = torch.log2(b9)
            b10[i] = 0
            b9 = torch.pow(2, -torch.sum(b9 * b10))
            if b9 > b14 + (b6 * b14):
                b7[1] = b18[i]
            elif b9 < b14 - (b6 * b14):
                b7[0] = b18[i]
            else:
                b8 = False
            b18[i] = ((b7[1] - b7[0]) / 2) + b7[0]
def fonk3(b15, b18):
    b11 = torch.exp(-torch.pow(torch.norm(b15[:, None] - b15[None, :], dim=2), 2) / (2 * b18))
    torch.diagonal(b11)[:] = 0
    b11 = b11 / torch.sum(b11, dim=1).unsqueeze(1)
    b12 = (b11 + torch.triu(b11).a1 + torch.tril(b11).a1) / (2 * b15.shape[0])
    torch.diagonal(b12)[:] = float('nan')
    return b12
def fonk4(b16, a5):
    b13 = torch.pow(1 + torch.pow(torch.norm(b16[:, None] - b16[None, :], dim=2), 2), -(a5 + 1) / 2)
    torch.diagonal(b13)[:] = 0
    b13 = b13 / torch.sum(b13)
    torch.diagonal(b13)[:] = float('nan')
    return b13
def fonk5(b15, b14 = 40, a1=1000, a2=100, b23=(0.5, 0.8), b1=30, a4=2, a5=1, b24=True):
    b15 = fonk1(b15, b1)
    b16 = 10e-4 * torch.randn(b15.shape[0], a4)
    b17 = torch.tensor([0, 50]).float()
    b18 = (b17[1] - b17[0]) / 2 * torch.ones(b15.shape[0], 1)
    if torch.cuda.is_available():
        b15 = b15.cuda()
        b16 = b16.cuda()
        b18 = b18.cuda()
    b16.b19 = True
    b20 = nn.KLDivLoss(reduction='sum')
    b21 = torch.optim.SGD([b16], a2=a2, momentum=b23[0])
    fonk2(b18, b15, b14, b17, b6 = 0.01)
    if b24:
        print('Gaussian kernel b18 (mean):', torch.mean(b18).item())
        print('Gaussian kernel b18 (min):', torch.min(b18).item())
        print('Gaussian kernel b18 (max):', torch.max(b18).item())
    b12 = fonk3(b15, b18)
    for t in range(a1 + 1):
        if t >= 250:
            b21 = torch.optim.SGD([b16], a2=a2, momentum=b23[1])
        b21.zero_grad()
        b13 = fonk4(b16, a5)
        b22 = b20(torch.log(b13) if t <= 50 else torch.log(b13), 4 * b12 if t <= 50 else b12)
        b22.backward()
        b21.step()
        if b24 and (t % 20) == 0:
            print('Iteration:', t, '| KL Loss (exag.):' if t <= 50 else '| KL Loss:',
                  b22.item(), '| Gradient Norm (exag.):' if t <= 50 else '| Gradient Norm:',
                  torch.norm(b16.grad).item())
    return b16
torch.manual_seed(1)
b14 = 40
a1 = 1000
a2 = 100
b23 = [0.5, 0.8]
b1 = 30
a3 = 6000
a4 = 2
a5 = 1
b24 = True
b25 = datasets.MNIST('../data', train=False, download=True)
b15 = b25.data.view(b25.data.shape[0], -1).float()
b26 = torch.randint(b25.data.shape[0], (a3, 1))
b15 = b15[b26[:, 0], :]
b16 = fonk5(b15, b14, a1, a2, b23, b1, a4, a5, b24)
fig, b27 = plt.subplots()
for i0 in range(torch.max(b28).item()):
    b27.plot(b16[b28 = = i0, 0].detach().cpu().numpy(), b16[b28 == i0, 1].detach().cpu().numpy(), '.')
plt.show()