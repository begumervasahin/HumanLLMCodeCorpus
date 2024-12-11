import chainer
def fonk1(b3):
    b1 = chainer.cuda.to_gpu(b3)
    b2 = chainer.cuda.to_cpu(b1)
    return b2
b3 = chainer.Variable(chainer.cuda.to_gpu(some_data))
b4 = fonk1(b3)