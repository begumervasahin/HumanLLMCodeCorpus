import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from torchvision import datasets
def pca(X, k=30):
    X = X / torch.max(X)
    X = X - torch.mean(X, dim=0)
    U, S, Vt = torch.svd(X)
    X_reduced = torch.mm(U[:, :k], torch.diag(S[:k]))
    return X_reduced
def gaussian_kernel_variance_search(variance, X, perp, variance_range, tol=0.01):
    n_samples = X.size(0)
    for i in range(n_samples):
        while True:
            H = torch.exp(-torch.norm(X[i] - X, dim=1) ** 2 / (2 * variance[i]))
            H[i] = 0
            H /= torch.sum(H)
            log_H = torch.log2(H)
            log_H[i] = 0
            H_shannon = torch.pow(2, -torch.sum(H * log_H))
            if H_shannon > perp + (tol * perp):
                variance_range[1] = variance[i]
            elif H_shannon < perp - (tol * perp):
                variance_range[0] = variance[i]
            else:
                break
            variance[i] = (variance_range[1] + variance_range[0]) / 2
def estimate_p(X, variance):
    P = torch.exp(-torch.norm(X[:, None] - X[None, :], dim=2) ** 2 / (2 * variance))
    torch.diagonal(P).zero_()
    P /= torch.sum(P, dim=1, keepdim=True)
    p = (P + P.T) / (2 * X.size(0))
    torch.diagonal(p).fill_(float('nan'))
    return p
def estimate_q(Y, v):
    q = torch.pow(1 + torch.norm(Y[:, None] - Y[None, :], dim=2) ** 2, -(v + 1) / 2)
    torch.diagonal(q).zero_()
    q /= torch.sum(q)
    torch.diagonal(q).fill_(float('nan'))
    return q
def tsne(X, perp=40, T=1000, lr=100, momentum=(0.5, 0.8), k=30, output_dim=2, v=1, verbose=True):
    n_samples = X.size(0)
    X_reduced = pca(X, k)
    Y = 1e-4 * torch.randn(n_samples, output_dim)
    variance_range = torch.tensor([0.0, 50.0])
    variance = torch.full((n_samples, 1), (variance_range[1] - variance_range[0]) / 2)
    if torch.cuda.is_available():
        X_reduced, Y, variance = X_reduced.cuda(), Y.cuda(), variance.cuda()
    Y.requires_grad = True
    loss_function = nn.KLDivLoss(reduction='sum')
    optimizer = torch.optim.SGD([Y], lr=lr, momentum=momentum[0])
    gaussian_kernel_variance_search(variance, X_reduced, perp, variance_range)
    if verbose:
        print(f'Gaussian kernel variance (mean): {torch.mean(variance).item()}')
        print(f'Gaussian kernel variance (min): {torch.min(variance).item()}')
        print(f'Gaussian kernel variance (max): {torch.max(variance).item()}')
    p = estimate_p(X_reduced, variance)
    for t in range(T + 1):
        if t == 250:
            optimizer = torch.optim.SGD([Y], lr=lr, momentum=momentum[1])
        optimizer.zero_grad()
        q = estimate_q(Y, v)
        if t <= 50:
            loss = loss_function(torch.log(q), 4 * p)
        else:
            loss = loss_function(torch.log(q), p)
        loss.backward()
        optimizer.step()
        if verbose and t % 20 == 0:
            print(f'Iteration: {t} | KL Loss: {loss.item()} | Gradient Norm: {torch.norm(Y.grad).item()}')
    return Y
def main():
    torch.manual_seed(1)
    perp = 40
    T = 1000
    lr = 100
    momentum = (0.5, 0.8)
    k = 30
    n_samples = 6000
    output_dim = 2
    v = 1
    verbose = True
    mnist = datasets.MNIST('../data', train=False, download=True)
    X = mnist.data.view(mnist.data.shape[0], -1).float()
    indices = torch.randint(mnist.data.shape[0], (n_samples,))
    X = X[indices]
    targets = mnist.targets[indices]
    Y = tsne(X, perp, T, lr, momentum, k, output_dim, v, verbose)
    plt.figure()
    for i in range(10):
        plt.scatter(Y[targets == i, 0].cpu().detach().numpy(), Y[targets == i, 1].cpu().detach().numpy(), label=str(i))
    plt.legend()
    plt.show()
if __name__ == "__main__":
    main()