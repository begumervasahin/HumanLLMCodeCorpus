import numpy as np
import json
import time
import os
import gc
from hyperopt import *
import torch
import torchvision
BATCH_SIZE = 300
mnist_train = torchvision.datasets.MNIST(
    "./data", train=True, download=True, transform=torchvision.transforms.ToTensor()
)
mnist_test = torchvision.datasets.MNIST(
    "./data", train=False, download=True, transform=torchvision.transforms.ToTensor()
)
dl_train = torch.utils.data.DataLoader(mnist_train, batch_size=BATCH_SIZE, shuffle=False)
dl_test = torch.utils.data.DataLoader(mnist_test, batch_size=10000, shuffle=False)
def test(model):
    for i, (features_, labels_) in enumerate(dl_test):
        features, labels = torch.reshape(features_, (10000, 28 * 28)), labels_
        pred = model.forward(features)
        return pred.argmax(dim=1).eq(labels).sum().item() / 10000 * 100
def train(model, epochs=3):
    stats = []
    for epoch in range(epochs):
        for i, (features_, labels_) in enumerate(dl_train):
            t0 = time.process_time()
            model.begin()
            features, labels = torch.reshape(features_, (BATCH_SIZE, 28 * 28)), labels_
            pred = model.forward(features)
            loss = torch.nn.functional.nll_loss(pred, labels)
            model.zero_grad()
            loss.backward(create_graph=True)
            model.adjust()
            tf = time.process_time()
            data = {
                "time": tf - t0,
                "iter": epoch * len(dl_train) + i,
                "loss": loss.item(),
                "params": {k: v.item() for k, v in model.optimizer.parameters.items() if "." not in k},
            }
            stats.append(data)
    return stats
def run_experiment(opt, name="out", usr={}, epochs=3):
    torch.manual_seed(0x42)
    model = MNIST_FullyConnected(28 * 28, 128, 10, opt)
    print("Running...", str(model))
    model.initialize()
    log = train(model, epochs)
    acc = test(model)
    out = {"acc": acc, "log": log, "usr": usr}
    with open(f"log/{name}.json", "w+") as f:
        json.dump(out, f, indent=True)
    times = [x["time"] for x in log]
    print("Times (ms):", np.mean(times), "+/-", np.std(times))
    print("Final accuracy:", acc)
    return out
def sgd_experiments():
    run_experiment(SGD(0.01), "sgd", epochs=1)
    out = run_experiment(SGD(0.01, optimizer=SGD(0.01)), "sgd+sgd", epochs=1)
    alpha = out["log"][-1]["params"]["alpha"]
    print(alpha)
    run_experiment(SGD(alpha), "sgd-final", epochs=1)
def adam_experiments():
    run_experiment(Adam(), "adam", epochs=1)
    print()
    mo = SGDPerParam(0.001, ["alpha", "beta1", "beta2", "log_eps"], optimizer=SGD(0.0001))
    out = run_experiment(Adam(optimizer=mo), "adam+sgd", epochs=1)
    p = out["log"][-1]["params"]
    alpha = p["alpha"]
    beta1 = Adam.clamp(torch.tensor(p["beta1"])).item()
    beta2 = Adam.clamp(torch.tensor(p["beta2"])).item()
    log_eps = p["log_eps"]
    print(alpha, beta1, beta2, log_eps)
    print(mo)
    run_experiment(
        Adam(alpha=p["alpha"], beta1=beta1, beta2=beta2, log_eps=log_eps),
        "adam+sgd-final",
        epochs=1,
    )
    print()
    out = run_experiment(Adam(optimizer=Adam()), "adam2", epochs=1)
    p = out["log"][-1]["params"]
    alpha = p["alpha"]
    beta1 = Adam.clamp(torch.tensor(p["beta1"])).item()
    beta2 = Adam.clamp(torch.tensor(p["beta2"])).item()
    log_eps = p["log_eps"]
    print(alpha, beta1, beta2, log_eps)
    run(
        Adam(alpha=p["alpha"], beta1=beta1, beta2=beta2, log_eps=log_eps),
        "adam2-final",
