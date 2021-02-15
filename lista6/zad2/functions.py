import numpy as np


class Sigmoid:
    def __call__(self, x):
        return 1.0 / (1 + np.exp(-x))

    def derivative(self, x):
        return x * (1.0 - x)


class ReLU:
    def __call__(self, x):
        return np.maximum(0, x)

    def derivative(self, x):
        return np.where(x > 0, 1, 0)


class Tanh:
    def __call__(self, x):
        return np.tanh(x)

    def derivative(self, x):
        return 1.0 - np.tanh(x) ** 2
