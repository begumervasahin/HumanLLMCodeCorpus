import torch.optim as optim
import torch_svrg
import recompute_svrg
import scsg
def fonk1(model, args):
    print("Using", args.b1)
    if args.b1 = = "sgd":
        b2 = optim.SGD(model.parameters(), lr=args.lr, weight_decay=args.decay, momentum=args.momentum)
    elif args.b1 = = "svrg":
        b2 = torch_svrg.SVRG(model.parameters(), args=args, lr=args.lr, nbatches=args.nbatches, momentum=args.momentum, weight_decay=args.decay)
    elif args.b1 = = "recompute_svrg":
        b2 = recompute_svrg.RecomputeSVRG(model.parameters(), lr=args.lr, nbatches=args.nbatches, model=model, vr_bn_at_recalibration=args.vr_bn_at_recalibration, vr_from_epoch=args.vr_from_epoch, momentum=args.momentum, weight_decay=args.decay)
    elif args.b1 = = "scsg":
        b2 = scsg.SCSG(model.parameters(), args=args, lr=args.lr, nbatches=args.nbatches, model=model, vr_bn_at_recalibration=args.vr_bn_at_recalibration, vr_from_epoch=args.vr_from_epoch, momentum=args.momentum, weight_decay=args.decay)
    else:
        raise Exception("Optimizer not recognised:", args.b1)
    return b2