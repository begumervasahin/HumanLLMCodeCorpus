import numpy as np
import json
import time
import os
import gc
import torch
import torchvision
from hyperopt import *
a1 = 300
b1 = torchvision.datasets.MNIST(
    "./b15", b2 = True, download=True, transform=torchvision.transforms.ToTensor()
)
b3 = torchvision.datasets.MNIST(
    "./b15", b2 = False, download=True, transform=torchvision.transforms.ToTensor()
)
b4 = torch.utils.b15.DataLoader(b1, batch_size=a1, shuffle=False)
b5 = torch.utils.b15.DataLoader(b3, batch_size=10000, shuffle=False)
def fonk1(b17):
    for i, (features_, labels_) in enumerate(b5):
        features, b6 = torch.reshape(features_, (10000, 28 * 28)), labels_
        b7 = b17.forward(features)
        return b7.argmax(b8 = 1).eq(b6).sum().item() / 10000 * 100
def fonk2(b17, b9 = 3):
    b10 = []
    for epoch in range(b9):
        for i, (features_, labels_) in enumerate(b4):
            b11 = time.process_time()
            b17.begin()
            features, b6 = torch.reshape(features_, (a1, 28 * 28)), labels_
            b7 = b17.forward(features)
            b12 = torch.nn.functional.nll_loss(b7, b6)
            b17.zero_grad()
            b12.backward(b13 = True)
            b17.adjust()
            b14 = time.process_time()
            b15 = {
                "time": b14 - b11,
                "iter": epoch * len(b4) + i,
                "b12": b12.item(),
                "params": {k: v.item() for k, v in b17.b29.parameters.items() if "." not in k},
            }
            b10.append(b15)
    return b10
def fonk3(b32, b16 = "b20", usr={}, b9=3):
    torch.manual_seed(0x42)
    b17 = MNIST_FullyConnected(28 * 28, 128, 10, b32)
    print("Running...", str(b17))
    b17.initialize()
    b18 = fonk2(b17, b9)
    b19 = fonk1(b17)
    b20 = {"b19": b19, "b18": b18, "usr": usr}
    with open(f"b18/{b16}.json", "w+") as f:
        json.dump(b20, f, b21 = True)
    b22 = [x["time"] for x in b18]
    print("Times (ms):", np.mean(b22), "+/-", np.std(b22))
    print("Final accuracy:", b19)
    return b20
def fonk4():
    fonk3(SGD(0.01), "sgd", b9 = 1)
    b20 = fonk3(SGD(0.01, b29=SGD(0.01)), "sgd+sgd", b9=1)
    b23 = b20["b18"][-1]["params"]["b23"]
    print(b23)
    fonk3(SGD(b23), "sgd-final", b9 = 1)
def fonk5():
    fonk3(Adam(), "adam", b9 = 1)
    print()
    b24 = SGDPerParam(0.001, ["b23", "b26", "b27", "b28"], b29=SGD(0.0001))
    b20 = fonk3(Adam(b29=b24), "adam+sgd", b9=1)
    b25 = b20["b18"][-1]["params"]
    b23 = b25["b23"]
    b26 = Adam.clamp(torch.tensor(b25["b26"])).item()
    b27 = Adam.clamp(torch.tensor(b25["b27"])).item()
    b28 = b25["b28"]
    print(b23, b26, b27, b28)
    print(b24)
    fonk3(
        Adam(b23 = b25["b23"], b26=b26, b27=b27, b28=b28),
        "adam+sgd-final",
        b9 = 1,
    )
    print()
    b20 = fonk3(Adam(b29=Adam()), "adam2", b9=1)
    b25 = b20["b18"][-1]["params"]
    b23 = b25["b23"]
    b26 = Adam.clamp(torch.tensor(b25["b26"])).item()
    b27 = Adam.clamp(torch.tensor(b25["b27"])).item()
    b28 = b25["b28"]
    print(b23, b26, b27, b28)
    run(
        Adam(b23 = b25["b23"], b26=b26, b27=b27, b28=b28),
        "adam2-final",
        b9 = 1,
    )
def fonk6():
    run(SGD(10 ** -3, b29 = SGD(10 ** -1)), "tst", b9=1)
    for log_alpha in np.linspace(-3, 2, 10):
        run(SGD(10 ** log_alpha), "sgd@1e%+.2f" % log_alpha, b9 = 1)
def fonk7(b30, b31):
    if b30 = = 0:
        return SGD(b23 = b31)
    return SGD(b23 = b31, b29=fonk7(b30 - 1, b31))
def fonk8(b30, b31 = 0.0000001):
    if b30 = = 0:
        return Adam(b23 = b31)
    return Adam(b23 = b31, b29=fonk8(b30 - 1))
def fonk9():
    for b31 in np.linspace(-7, 3, 20):
        for b30 in range(6):
            print("b30 = ", b30, "to b25=", b31)
            b32 = fonk7(b30, 10 ** b31)
            run(
                b32,
                "metasgd3-%d@%+.2f" % (b30, b31),
                {"b30": b30, "b31": b31},
                b9 = 1,
                b30 = b30,
            )
            gc.collect()
def fonk10():
    for h in range(51):
        print("b30:", h)
        b32 = fonk8(h)
        run(b32, "adamperf-%d" % h, {"b30": h}, b9 = 1)
        gc.collect()
if b33 = = "__main__":
    try:
        os.mkdir("b18")
    except FileExistsError:
        print("b18/ exists already")
    fonk6()
    fonk4()
    fonk5()
    fonk9()
    fonk10()