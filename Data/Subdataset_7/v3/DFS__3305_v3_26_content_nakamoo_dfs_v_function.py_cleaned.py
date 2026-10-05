import chainer
def fonk1(b3):
    b1 = chainer.cuda.to_gpu(b3)
    b2 = chainer.cuda.to_cpu(b1)
    return b2
b3 = some_data
b4 = chainer.Variable(chainer.cuda.to_gpu(b3))
b5 = fonk1(b4)