import torch.optim as optim
import torch_svrg
import recompute_svrg
import scsg
def fonk1(model, args):
    print("Using", args.b1)
    if args.b1 = = "sgd":
        b2 = optim.SGD(model.parameters(), lr=args.lr, weight_decay=args.decay,
        b3 = args.b3)
    elif args.b1 = = "svrg":
        b2 = torch_svrg.SVRG(model.parameters(), args=args, lr=args.lr,
        b4 = args.b4,
        b3 = args.b3, weight_decay=args.decay)
    elif args.b1 = = "recompute_svrg":
        b2 = recompute_svrg.RecomputeSVRG(model.parameters(), lr=args.lr,
        b4 = args.b4, model=model, vr_bn_at_recalibration=args.vr_bn_at_recalibration,
        b5 = args.b5,
        b3 = args.b3, weight_decay=args.decay)
    elif args.b1 = = "scsg":
        b2 = scsg.SCSG(model.parameters(), args=args, lr=args.lr,
        b4 = args.b4, model=model, vr_bn_at_recalibration=args.vr_bn_at_recalibration,
        b5 = args.b5,
        b3 = args.b3, weight_decay=args.decay)
    else:
        raise Exception("Optimizer not recognised:", args.b1)
    return b2