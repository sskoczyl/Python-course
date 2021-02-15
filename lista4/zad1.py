import time
from functools import wraps


def measure_time(subject):
    @wraps(subject)
    def measurement(*args):
        start = time.time()
        returned_value = subject(*args)
        finish = time.time()

        print("Execution time of:", subject.__name__, finish - start)
        return returned_value

    return measurement


@measure_time
def some_function(*args):
    time.sleep(1)

    return args


@measure_time
def raise_to_power(x, y):
    out = 1

    for i in range(0, y):
        out *= x

    return out


print(some_function('This', 'is', 'some function'))
print("2^3=", raise_to_power(2, 3))
