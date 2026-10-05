import torch
from torchvision import datasets, transforms
from torch.autograd import Variable
def create_sequential_MNIST(batch_size, input_size, gpu=True, dataset_folder='./data'):
    kwargs = {'num_workers': 0, 'pin_memory': True} if gpu else {}
    permute_mask = torch.randperm(784)
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,)),
        transforms.Lambda(lambda x: x.view(-1, input_size)),
        transforms.Lambda(lambda x: x[permute_mask])
    ])
    train_loader = torch.utils.data.DataLoader(
        datasets.MNIST(dataset_folder, train=True, download=True, transform=transform),
        batch_size=batch_size, shuffle=True, drop_last=True, **kwargs)
    test_loader = torch.utils.data.DataLoader(
        datasets.MNIST(dataset_folder, train=False, transform=transform),
        batch_size=batch_size, shuffle=False, drop_last=True, **kwargs)
    return train_loader, test_loader
def train_model(model, train_loader, val_loader, test_loader, criterion, args, optimizer):
    model.train()
    test_accuracy = []
    train_accuracy = []
    correct = 0
    for current_batch, ((data, target), (val_data, _)) in enumerate(zip(train_loader, val_loader)):
        if args.gpu:
            data, target, val_data = data.cuda(), target.cuda(), val_data.cuda()
        data, target, val_data = Variable(data), Variable(target), Variable(val_data)
        model.zero_grad()
        model.hidden = model.init_hidden()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), args.gradient_clipping_value)
        def validation_eval():
            model.hidden = model.init_hidden()
            return torch.exp(model(val_data))
        if args.opt in ['hcadam', 'hcgd']:
            optimizer.step(validation_eval=validation_eval)
        else:
            optimizer.step()
        pred = output.data.max(1, keepdim=True)[1]
        correct += pred.eq(target.data.view_as(pred)).sum() if (current_batch > 0) else 0
        if (args.log_interval > 0) and (current_batch > 0) and (current_batch % args.log_interval == 0):
            acc = 100. * correct / (args.batch_size * args.log_interval)
            train_accuracy.append(acc)
            correct = 0
            tl, te = evaluate_model(model, test_loader, criterion, args, n_examples=1000)
            print(f'Batch {current_batch}: Train accuracy ({acc:.5f}%) Loss: {loss.item():.6f} Test accuracy ({te:.5f}%) Loss: {tl:.6f}')
            test_accuracy.append(te)
    return train_accuracy, test_accuracy
def evaluate_model(model, test_loader, criterion, args, n_examples):
    model.eval()
    total = 0
    test_loss = 0
    correct = 0
    i = 0
    for data, target in test_loader:
        total += target.size(0)
        if args.gpu:
            data, target = data.cuda(), target.cuda()
        with torch.no_grad():
            data, target = Variable(data), Variable(target)
            output = model(data)
            test_loss += criterion(output, target).item()
        pred = output.data.max(1, keepdim=True)[1]
        correct += pred.eq(target.data.view_as(pred)).sum()
        i += args.batch_size
        if i > n_examples:
            break
    test_loss /= i
    acc = 100. * float(correct) / i
    model.train()
    return test_loss, acc