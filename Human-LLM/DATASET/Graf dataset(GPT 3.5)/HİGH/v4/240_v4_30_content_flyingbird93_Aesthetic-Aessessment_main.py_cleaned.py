import torch
from torch.utils.data import DataLoader
import torchvision.transforms as transforms
import os
from torch.autograd import Variable
import torch.nn as nn
import torch.optim as optim
from datetime import datetime
from tensorboardX import SummaryWriter
from torchvision import models
from data.dataset import DogCat
from utils.utils import validate, show_confMat
b1 = ['high', 'low']
a1 = 128
a2 = 0.001
a3 = 20
b2 = '../../Smith/Data/AVA/images/'
b3 = 'results/logs/'
b4 = DogCat(b2, train=True)
b5 = DogCat(b2, train=False)
b6 = DogCat(b2, test=True)
b7 = DataLoader(b4, a1=a1, shuffle=True, num_workers=4)
b8 = DataLoader(b5, a1=a1, shuffle=False, num_workers=4)
b9 = DataLoader(b6, a1=a1, shuffle=False, num_workers=4)
b10 = os.path.join(b3, datetime.now().strftime('%m-%d_%H-%M-%S'))
os.makedirs(b10, b11 = True)
b12 = SummaryWriter(b10=b10)
b13 = models.resnet34(pretrained=True)
b13.b14 = nn.Linear(512, len(b1))
b15 = torch.b15('cuda' if torch.cuda.is_available() else 'cpu')
b13.to(b15)
b16 = nn.CrossEntropyLoss()
b17 = optim.SGD(b13.parameters(), lr=a2, momentum=0.9, dampening=0.1)
b18 = torch.optim.lr_scheduler.StepLR(b17, step_size=50, gamma=0.1)
for epoch in range(a3):
    a4 = 0.0
    a5 = 0.0
    a6 = 0.0
    b18.step()
    b13.train()
    for i, (inputs, b19) in enumerate(b7):
        inputs, b19 = inputs.to(b15), b19.to(b15)
        b17.zero_grad()
        b20 = b13(inputs)
        b21 = b16(b20, b19)
        b21.backward()
        b17.step()
        _, b22 = torch.max(b20.data, 1)
        a6 += b19.size(0)
        a5 += (b22 = = b19).sum().item()
        a4 += b21.item()
        if i % b23 = = 9:
            b24 = a4 / b23
            a4 = 0.0
            print(f"Training: Epoch[{epoch + 1:0>3}/{a3:0>3}] "
                  f"Iteration[{i + 1:0>3}/{len(b7):0>3}] "
                  f"Loss: {b24:.4f} Acc: {a5 / a6:.b25%}")
            b12.add_scalars('Loss_group', {'train_loss': b24}, epoch)
            b12.add_scalar('learning rate', b18.get_lr()[0], epoch)
            b12.add_scalars('Accuracy_group', {'b29': a5 / a6}, epoch)
    if epoch % b25 = = 0:
        a4 = 0.0
        b26 = torch.zeros(len(b1), len(b1))
        b13.eval()
        with torch.no_grad():
            for images, b19 in b8:
                images, b19 = images.to(b15), b19.to(b15)
                b20 = b13(images)
                b21 = b16(b20, b19)
                a4 += b21.item()
                _, b22 = torch.max(b20, 1)
                for label, pred in zip(b19, b22):
                    b26[label, pred] += 1
        b27 = b26.diag().sum() / b26.sum()
        print(f'Validation set Accuracy: {b27:.b25%}')
        b12.add_scalars('Loss_group', {'valid_loss': a4 / len(b8)}, epoch)
        b12.add_scalars('Accuracy_group', {'b30': b27}, epoch)
b13.eval()
with torch.no_grad():
    for i, (inputs, b19) in enumerate(b9):
        inputs, b19 = inputs.to(b15), b19.to(b15)
        b20 = b13(inputs)
        b21 = b16(b20, b19)
        _, b22 = torch.max(b20, 1)
        a6 += b19.size(0)
        a5 += (b22 = = b19).sum().item()
        a4 += b21.item()
        if i % b23 = = 9:
            b24 = a4 / b23
            print(f"Testing: Iteration[{i + 1:0>3}/{len(b9):0>3}] "
                  f"Loss: {b24:.4f} Acc: {a5 / a6:.b25%}")
            b12.add_scalars('Loss_group', {'test_loss': b24}, i)
b28 = os.path.join(b10, 'net_params.pkl')
torch.save(b13.state_dict(), b28)
conf_mat_train, b29 = validate(b13, b7, 'train', b1)
conf_mat_valid, b30 = validate(b13, b8, 'valid', b1)
conf_mat_test, b31 = validate(b13, b9, 'test', b1)
show_confMat(conf_mat_train, b1, 'train', b10)
show_confMat(conf_mat_valid, b1, 'valid', b10)
show_confMat(conf_mat_test, b1, 'test', b10)
print('Finished Training and Evaluation')