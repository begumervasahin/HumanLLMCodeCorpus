import chainer
def move_between_cpu_and_gpu(data):
    data_on_gpu = chainer.cuda.to_gpu(data)
    data_on_cpu = chainer.cuda.to_cpu(data_on_gpu)
    return data_on_cpu
data = some_data
data_variable = chainer.Variable(chainer.cuda.to_gpu(data))
result = move_between_cpu_and_gpu(data_variable)