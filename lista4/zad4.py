import math
from inspect import getfullargspec


class FuncSpace(object):
    func_list = dict()

    @staticmethod
    def add_function(fn):
        func = Func(fn)
        FuncSpace.func_list[func.signature()] = fn
        return func


class Func(object):

    def __init__(self, fn):
        self.function = fn

    def __call__(self, *args, **kwargs):
        fn = FuncSpace.func_list.get(self.signature(args=args))
        return fn(*args, **kwargs)

    def signature(self, args=None):
        if args is None:
            args = getfullargspec(self.function).args
        return tuple([len(args), self.function.__class__, self.function.__name__, self.function.__module__])


def overload(fn):
    space = FuncSpace()
    return space.add_function(fn)


@overload
def area(a, b):
    return a * b


@overload
def area(a):
    return 3.14 * a ** 2


@overload
def norm(x, y):
    return math.sqrt(x * x + y * y)


@overload
def norm(x, y, z):
    return abs(x) + abs(y) + abs(z)


print("Pole prostokata: ", area(2, 3), " Kola:", area(2))
print("Norma euklidesowa: ", norm(2, 4), " Taksowkowa:", norm(2, 3, 4))
