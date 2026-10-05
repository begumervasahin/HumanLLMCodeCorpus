import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from torchvision import datasets
def pca(X, k=30):
    X_normalized = X / torch.max(X)
    X_centered = X_normalized - torch.mean(X_normalized, dim=0)
    U, S, Vt = torch.svd(X_centered)
    X_pca = torch.mm(U[:, :k], torch.diag(S[:k]))
    return X_pca
def gaussian_kernel_variance_search(variance, X, perp, vr, tol=0.01):
    for i in range(X.shape[0]):
        variance_range = vr.clone()
        binary_search = True
        while binary_search:
            H = torch.exp(-torch.pow(torch.norm(X[i, :] - X, dim=1), 2) / (2 * variance[i]))
            H[i] = 0
            H = H / torch.sum(H)
            log_H = torch.log2(H)
            log_H[i] = 0
            H = torch.pow(2, -torch.sum(H * log_H))
            if H > perp + (tol * perp):
                variance_range[1] = variance[i]
            elif H < perp - (tol * perp):
                variance_range[0] = variance[i]
            else:
                binary_search = False
            variance[i] = ((variance_range[1] - variance_range[0]) / 2) + variance_range[0]
def estimate_p(X, variance):
    P = torch.exp(-torch.pow(torch.norm(X[:, None] - X[None, :], dim=2), 2) / (2 * variance))
    torch.diagonal(P)[:] = 0
    P = P / torch.sum(P, dim=1).unsqueeze(1)
    p = (P + torch.triu(P).T + torch.tril(P).T) / (2 * X.shape[0])
    torch.diagonal(p)[:] = float('nan')
    return p
def estimate_q(Y, v):
    q = torch.pow(1 + torch.pow(torch.norm(Y[:, None] - Y[None, :], dim=2), 2), -(v + 1) / 2)
    torch.diagonal(q)[:] = 0
    q = q / torch.sum(q)
    torch.diagonal(q)[:] = float('nan')
    return q
def tsne(X, perp=40, T=1000, lr=100, a=(0.5, 0.8), k=30, M=2, v=1, verbose=True):
    X = pca(X, k)
    Y = 10e-4 * torch.randn(X.shape[0], M)
    vr = torch.tensor([0, 50]).float()
    variance = (vr[1] - vr[0]) / 2 * torch.ones(X.shape[0], 1)
    if torch.cuda.is_available():
        X = X.cuda()
        Y = Y.cuda()
        variance = variance.cuda()
    Y.requires_grad = True
    loss_function = nn.KLDivLoss(reduction='sum')
    optimizer = torch.optim.SGD([Y], lr=lr, momentum=a[0])
    gaussian_kernel_variance_search(variance, X, perp, vr, tol=0.01)
    if verbose:
        print('Gaussian kernel variance (mean):', torch.mean(variance).item())
        print('Gaussian kernel variance (min):', torch.min(variance).item())
        print('Gaussian kernel variance (max):', torch.max(variance).item())
    p = estimate_p(X, variance)
    for t in range(T + 1):
        if t >= 250:
            optimizer = torch.optim.SGD([Y], lr=lr, momentum=a[1])
        optimizer.zero_grad()
        q = estimate_q(Y, v)
        loss = loss_function(torch.log(q) if t <= 50 else torch.log(q), 4 * p if t <= 50 else p)
        loss.backward()
        optimizer.step()
        if verbose and (t % 20) == 0:
            print('Iteration:', t, '| KL Loss (exag.):' if t <= 50 else '| KL Loss:',
                  loss.item(), '| Gradient Norm (exag.):' if t <= 50 else '| Gradient Norm:',
                  torch.norm(Y.grad).item())
    return Y
torch.manual_seed(1)
perp = 40
T = 1000
lr = 100
a = [0.5, 0.8]
k = 30
n = 6000
M = 2
v = 1
verbose = True
mnist = datasets.MNIST('../data', train=False, download=True)
X = mnist.data.view(mnist.data.shape[0], -1).float()
index = torch.randint(mnist.data.shape[0], (n, 1))
X = X[index[:, 0], :]
Y = tsne(X, perp, T, lr, a, k, M, v, verbose)
fig, ax = plt.subplots()
for i0 in range(torch.max(targets).item()):
    ax.plot(Y[targets == i0, 0].detach().cpu().numpy(), Y[targets == i0, 1].detach().cpu().numpy(), '.')
plt.show()