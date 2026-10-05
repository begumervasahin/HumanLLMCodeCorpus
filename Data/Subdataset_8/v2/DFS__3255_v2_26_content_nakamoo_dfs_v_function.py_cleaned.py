import chainer
def move_between_cpu_gpu(var):
    var_on_gpu = chainer.cuda.to_gpu(var)
    var_on_cpu = chainer.cuda.to_cpu(var_on_gpu)
    return var_on_cpu
var = chainer.Variable(chainer.cuda.to_gpu(some_data))
result = move_between_cpu_gpu(var)