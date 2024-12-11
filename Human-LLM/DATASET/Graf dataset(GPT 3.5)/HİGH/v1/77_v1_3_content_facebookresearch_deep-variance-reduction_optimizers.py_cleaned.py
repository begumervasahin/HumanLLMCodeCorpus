import torch.optim as optim
import torch_svrg
import recompute_svrg
import scsg
def fonk1(b11, b10):
    print("Using", b10.b1)
    if b10.b1 = = "sgd":
        b2 = optim.SGD(b11.b9(), b7=b10.b7, weight_decay=b10.b8,
                              b3 = b10.b3)
    elif b10.b1 = = "svrg":
        b2 = torch_svrg.SVRG(b11.b9(), b10=b10, b7=b10.b7,
                                     b4 = b10.b4,
                                     b3 = b10.b3, weight_decay=b10.b8)
    elif b10.b1 = = "recompute_svrg":
        b2 = recompute_svrg.RecomputeSVRG(b11.b9(), b7=b10.b7,
                                                 b4 = b10.b4, b11=b11,
                                                 b5 = b10.b5,
                                                 b6 = b10.b6,
                                                 b3 = b10.b3, weight_decay=b10.b8)
    elif b10.b1 = = "scsg":
        b2 = scsg.SCSG(b11.b9(), b10=b10, b7=b10.b7,
                              b4 = b10.b4, b11=b11,
                              b5 = b10.b5,
                              b6 = b10.b6,
                              b3 = b10.b3, weight_decay=b10.b8)
    else:
        raise Exception("Optimizer not recognised:", b10.b1)
    return b2
class class1:
    def fonk2(self, b1, b7, b8, b3, b4, b5, b6):
        self.b1 = b1
        self.b7 = b7
        self.b8 = b8
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
class class2:
    def fonk3(self):
        self.b9 = lambda: "Parameters"
b10 = class1(b1="svrg", b7=0.01, b8=0.0001, b3=0.9, b4=100, b5=False, b6=1)
b11 = class2()
b12 = fonk1(b11, b10)