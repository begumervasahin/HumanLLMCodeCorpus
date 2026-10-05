import torch.optim as optim
import torch_svrg
import recompute_svrg
import scsg
class class1:
    def fonk1(self, b1, b2, b3, b4, b5, b6, b7):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
class class2:
    def fonk2(self):
        self.b8 = lambda: "Parameters"
def fonk3(b11, b10):
    print("Selected b9 b1:", b10.b1)
    if b10.b1 = = "sgd":
        b9 = optim.SGD(b11.b8(), b2=b10.b2, weight_decay=b10.b3, b4=b10.b4)
    elif b10.b1 = = "svrg":
        b9 = torch_svrg.SVRG(b11.b8(), b10=b10, b2=b10.b2,
                                    b5 = b10.b5, b4=b10.b4, weight_decay=b10.b3)
    elif b10.b1 = = "recompute_svrg":
        b9 = recompute_svrg.RecomputeSVRG(b11.b8(), b2=b10.b2,
                                                b5 = b10.b5, b11=b11,
                                                b6 = b10.b6,
                                                b7 = b10.b7,
                                                b4 = b10.b4, weight_decay=b10.b3)
    elif b10.b1 = = "scsg":
        b9 = scsg.SCSG(b11.b8(), b10=b10, b2=b10.b2,
                              b5 = b10.b5, b11=b11,
                              b6 = b10.b6,
                              b7 = b10.b7,
                              b4 = b10.b4, weight_decay=b10.b3)
    else:
        raise ValueError("Unknown b9 b1:", b10.b1)
    return b9
b10 = class1(b1="svrg", b2=0.01, b3=0.0001, b4=0.9, b5=100, b6=False, b7=1)
b11 = class2()
b9 = fonk3(b11, b10)