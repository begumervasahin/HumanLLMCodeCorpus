import torch.optim as optim
import torch_svrg
import recompute_svrg
import scsg
def optimizer(model, args):
    method = args.method
    lr = args.lr
    decay = args.decay
    momentum = args.momentum
    nbatches = args.nbatches
    vr_bn_at_recalibration = args.vr_bn_at_recalibration
    vr_from_epoch = args.vr_from_epoch
    print("Using", method)
    if method == "sgd":
        optimizer = optim.SGD(model.parameters(), lr=lr, weight_decay=decay, momentum=momentum)
    elif method == "svrg":
        optimizer = torch_svrg.SVRG(model.parameters(), args=args, lr=lr, nbatches=nbatches, momentum=momentum, weight_decay=decay)
    elif method == "recompute_svrg":
        optimizer = recompute_svrg.RecomputeSVRG(model.parameters(), lr=lr, nbatches=nbatches, model=model, vr_bn_at_recalibration=vr_bn_at_recalibration, vr_from_epoch=vr_from_epoch, momentum=momentum, weight_decay=decay)
    elif method == "scsg":
        optimizer = scsg.SCSG(model.parameters(), args=args, lr=lr, nbatches=nbatches, model=model, vr_bn_at_recalibration=vr_bn_at_recalibration, vr_from_epoch=vr_from_epoch, momentum=momentum, weight_decay=decay)
    else:
        raise Exception("Optimizer not recognised:", method)
    return optimizer