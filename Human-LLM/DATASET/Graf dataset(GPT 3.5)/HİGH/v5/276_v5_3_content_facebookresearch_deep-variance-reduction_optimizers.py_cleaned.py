import torch.optim as optim
import torch_svrg
import recompute_svrg
import scsg
def fonk1(model, args):
    b1 = args.b1
    b2 = args.b2
    b3 = args.b3
    b4 = args.b4
    b5 = args.b5
    b6 = args.b6
    b7 = args.b7
    print("Using", b1)
    if b1 = = "sgd":
        b8 = optim.SGD(model.parameters(), b2=b2, weight_decay=b3, b4=b4)
    elif b1 = = "svrg":
        b8 = torch_svrg.SVRG(model.parameters(), args=args, b2=b2, b5=b5, b4=b4, weight_decay=b3)
    elif b1 = = "recompute_svrg":
        b8 = recompute_svrg.RecomputeSVRG(model.parameters(), b2=b2, b5=b5, model=model, b6=b6, b7=b7, b4=b4, weight_decay=b3)
    elif b1 = = "scsg":
        b8 = scsg.SCSG(model.parameters(), args=args, b2=b2, b5=b5, model=model, b6=b6, b7=b7, b4=b4, weight_decay=b3)
    else:
        raise Exception("Optimizer not recognised:", b1)
    return b8