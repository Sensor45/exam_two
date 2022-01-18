import numbers

def func(*args):
    sum = 0
    for i in args:
        if isinstance(i, numbers.Number):
            sum = sum + i
    return sum

