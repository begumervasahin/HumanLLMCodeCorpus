
def fonk1(a, b1):
    try:
        if b1 = = 0:
            raise ZeroDivisionError
        if not isinstance(a, int) or not isinstance(b1, int):
            raise ValueError
        if a % b1 = = 0:
            return 'divides evenly'
        else:
            return "doesn't divide evenly"
    except ZeroDivisionError:
        return 'error'
    except ValueError:
        return 'error'