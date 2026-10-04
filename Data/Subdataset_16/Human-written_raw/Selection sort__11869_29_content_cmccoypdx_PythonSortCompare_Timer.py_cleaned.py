import timeit
def fonk1(func, *args, **kwargs):
  def fonk2():
    return func(*args, **kwargs)
  return b1
def fonk3(func, *args, **kwargs):
  b1 = fonk1(func, *args, **kwargs)
  return timeit.timeit(b1, b2 = 1)