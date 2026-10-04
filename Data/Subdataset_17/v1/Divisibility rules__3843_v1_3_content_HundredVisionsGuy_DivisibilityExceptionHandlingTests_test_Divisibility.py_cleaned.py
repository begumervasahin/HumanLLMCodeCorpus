
def divisibility(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError
        if a % b == 0:
            return 'divides evenly'
        else:
            return "doesn't divide evenly"
    except ZeroDivisionError:
        return 'error'
    except ValueError:
        return 'error'