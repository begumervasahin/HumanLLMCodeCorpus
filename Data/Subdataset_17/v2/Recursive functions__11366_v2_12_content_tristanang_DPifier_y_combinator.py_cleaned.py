import inspect
class DPifier:
    def __init__(self, f, lambda_mode=False):
        self.dp = {}
        self.Y = self.create_memoized_function()
        self.f = f if lambda_mode else self._parse_function(f)
    def __call__(self, *args):
        return self.Y(self.f)(*args)
    def create_memoized_function(self):
        def memoizer(f):
            def wrapper(*args):
                if args in self.dp:
                    return self.dp[args]
                else:
                    result = f(memoizer(f))(*args)
                    self.dp[args] = result
                    return result
            return wrapper
        return memoizer
    def _parse_function(self, f):
        function_name = f.__name__
        source_code = inspect.getsource(f)
        modified_code = source_code.replace(function_name, 'inner_func', 1).replace(f"{function_name}(", "wrapped_func(", 1)
        def wrapper_function(wrapped_func):
            exec(modified_code, {'wrapped_func': wrapped_func}, globals())
            return inner_func
        return wrapper_function
def factorial(f):
    def inner_func(n):
        if n == 0:
            return 1
        else:
            return n * f(n - 1)
    return inner_func
dp_factorial = DPifier(factorial)
print(dp_factorial(5))
