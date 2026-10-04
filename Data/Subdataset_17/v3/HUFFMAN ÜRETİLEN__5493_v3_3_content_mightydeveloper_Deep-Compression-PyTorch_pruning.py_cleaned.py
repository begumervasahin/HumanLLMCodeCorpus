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
os.makedirs('saves', exist_ok=True)
def parse_arguments():
    parser = argparse.ArgumentParser(description='PyTorch MNIST pruning from deep compression paper')
    parser.add_argument('--batch-size', type=int, default=50, metavar='N',
                        help='input batch size for training (default: 50)')
    parser.add_argument('--test-batch-size', type=int, default=1000, metavar='N',
                        help='input batch size for testing (default: 1000)')
    parser.add_argument('--epochs', type=int, default=100, metavar='N',
                        help='number of epochs to train (default: 100)')
    parser.add_argument('--lr', type=float, default=0.01, metavar='LR',
                        help='learning rate (default: 0.01)')
    parser.add_argument('--no-cuda', action='store_true', default=False,
                        help='disables CUDA training')
    parser.add_argument('--seed', type=int, default=42, metavar='S',
                        help='random seed (default: 42)')
    parser.add_argument('--log-interval', type=int, default=10, metavar='N',
                        help='how many batches to wait before logging training status')
    parser.add_argument('--log', type=str, default='log.txt',
                        help='log file name')
    parser.add_argument('--sensitivity', type=float, default=2,
                        help="sensitivity value that is multiplied to layer's std in order to get threshold value")
    return parser.parse_args()
def setup_device_and_seed(args):
    torch.manual_seed(args.seed)
    use_cuda = not args.no_cuda and torch.cuda.is_available()
    device = torch.device("cuda" if use_cuda else "cpu")
    if use_cuda:
        print("Using CUDA!")
        torch.cuda.manual_seed(args.seed)
    else:
        print("Not using CUDA.")
    return device
def get_data_loaders(args, use_cuda):
    kwargs = {'num_workers': 5, 'pin_memory': True} if use_cuda else {}
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    train_loader = torch.utils.data.DataLoader(
        datasets.MNIST('data', train=True, download=True, transform=transform),
        batch_size=args.batch_size, shuffle=True, **kwargs)
    test_loader = torch.utils.data.DataLoader(
        datasets.MNIST('data', train=False, transform=transform),
        batch_size=args.test_batch_size, shuffle=False, **kwargs)
    return train_loader, test_loader
def train_one_epoch(model, train_loader, optimizer, device, epoch, args):
    model.train()
    pbar = tqdm(enumerate(train_loader), total=len(train_loader))
    for batch_idx, (data, target) in pbar:
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        for name, p in model.named_parameters():
            if 'mask' not in name:
                tensor = p.data.cpu().numpy()
                grad_tensor = p.grad.data.cpu().numpy()
                grad_tensor = np.where(tensor == 0, 0, grad_tensor)
                p.grad.data = torch.from_numpy(grad_tensor).to(device)
        optimizer.step()
        if batch_idx % args.log_interval == 0:
            done = batch_idx * len(data)
            percentage = 100. * batch_idx / len(train_loader)
            pbar.set_description(f'Epoch: {epoch} [{done}/{len(train_loader.dataset)} ({percentage:.0f}%)] Loss: {loss.item():.6f}')
def train_model(model, train_loader, optimizer, device, args):
    for epoch in range(args.epochs):
        train_one_epoch(model, train_loader, optimizer, device, epoch, args)
def test_model(model, test_loader, device):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            test_loss += F.nll_loss(output, target, reduction='sum').item()
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()
    test_loss /= len(test_loader.dataset)
    accuracy = 100. * correct / len(test_loader.dataset)
    print(f'Test set: Average loss: {test_loss:.4f}, Accuracy: {correct}/{len(test_loader.dataset)} ({accuracy:.2f}%)')
    return accuracy
def main():
    args = parse_arguments()
    device = setup_device_and_seed(args)
    train_loader, test_loader = get_data_loaders(args, device.type == "cuda")
    model = LeNet(mask=True).to(device)
    print(model)
    util.print_model_parameters(model)
    optimizer = optim.Adam(model.parameters(), lr=args.lr, weight_decay=0.0001)
    initial_optimizer_state = optimizer.state_dict()
    print("--- Initial training ---")
    train_model(model, train_loader, optimizer, device, args)
    initial_accuracy = test_model(model, test_loader, device)
    util.log(args.log, f"initial_accuracy {initial_accuracy}")
    torch.save(model, 'saves/initial_model.ptmodel')
    print("--- Before pruning ---")
    util.print_nonzeros(model)
    model.prune_by_std(args.sensitivity)
    pruned_accuracy = test_model(model, test_loader, device)
    util.log(args.log, f"accuracy_after_pruning {pruned_accuracy}")
    print("--- Retraining ---")
    util.print_nonzeros(model)
    optimizer.load_state_dict(initial_optimizer_state)
    train_model(model, train_loader, optimizer, device, args)
    final_accuracy = test_model(model, test_loader, device)
    torch.save(model, 'saves/model_after_retraining.ptmodel')
    util.log(args.log, f"accuracy_after_retraining {final_accuracy}")
    print("--- After Retraining ---")
    util.print_nonzeros(model)
if __name__ == "__main__":
    main()