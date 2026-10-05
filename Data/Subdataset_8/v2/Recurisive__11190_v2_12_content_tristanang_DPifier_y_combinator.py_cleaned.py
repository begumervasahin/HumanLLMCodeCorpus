import inspect
class DPifier:
    def __init__(self, f, lambda_mode=False):
        self.dp = {}
        def Y(f):
            def g(*args):
                if args in self.dp:
                    return self.dp[args]
                else:
                    self.dp[args] = f(Y(f))(*args)
                    return self.dp[args]
            return g
        self.Y = Y
        if lambda_mode:
            self.f = f
        else:
            self.f = self.__parse_function(f)
    def __call__(self, *args):
        return self.Y(self.f)(*args)
    def __parse_function(self, f):
        functionName = f.__name__
        source_code = inspect.getsource(f)
        source_code = source_code.replace(functionName, 'h', 1)
        source_code = source_code.replace(functionName + '(', 'abc' + '(')
        def g(abc):
            exec(source_code, {'abc': abc}, globals())
            return h
        return g
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
dp_fibonacci = DPifier(fibonacci)
print(dp_fibonacci(10))
