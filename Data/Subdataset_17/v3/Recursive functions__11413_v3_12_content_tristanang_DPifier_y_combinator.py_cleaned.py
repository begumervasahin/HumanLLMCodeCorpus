import inspect
class DPifier:
    def __init__(self, func, lambda_mode=False):
        self.dp = {}
        self.Y = self._create_memoized_function()
        self.func = func if lambda_mode else self._parse_function(func)
    def __call__(self, *args):
        return self.Y(self.func)(*args)
    def _create_memoized_function(self):
        def memoizer(func):
            def wrapper(*args):
                if args in self.dp:
                    return self.dp[args]
                else:
                    result = func(memoizer(func))(*args)
                    self.dp[args] = result
                    return result
            return wrapper
        return memoizer
    def _parse_function(self, func):
        function_name = func.__name__
        source_code = inspect.getsource(func)
        modified_code = source_code.replace(function_name, 'inner_func', 1)
        modified_code = modified_code.replace(f"{function_name}(", "wrapped_func(", 1)
        def wrapper_function(wrapped_func):
            exec(modified_code, {'wrapped_func': wrapped_func}, globals())
            return inner_func
        return wrapper_function
def factorial(func):
    def inner_func(n):
        if n == 0:
            return 1
        else:
            return n * func(n - 1)
    return inner_func
dp_factorial = DPifier(factorial)
print(dp_factorial(5))
