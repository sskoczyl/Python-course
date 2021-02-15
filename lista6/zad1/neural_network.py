import numpy as np


class NeuralNetwork:
    def __init__(self, x, y, f1, f2):
        self.function1 = f1
        self.function2 = f2
        self.input = x
        self.weights1 = np.random.rand(4, self.input.shape[1])
        self.weights2 = np.random.rand(1, 4)
        self.y = y
        self.output = np.zeros(self.y.shape)
        self.eta = 0.5
        self.layer1 = self.function1(np.dot(self.input, self.weights1.T))

    def feed_forward(self):
        self.layer1 = self.function1(np.dot(self.input, self.weights1.T))
        self.output = self.function2(np.dot(self.layer1, self.weights2.T))

    def back_prop(self):
        delta2 = (self.y - self.output) * self.function2.derivative(self.output)
        d_weights2 = self.eta * np.dot(delta2.T, self.layer1)

        delta1 = self.function1.derivative(self.layer1) * np.dot(delta2, self.weights2)
        d_weights1 = self.eta * np.dot(delta1.T, self.input)

        self.weights1 += d_weights1
        self.weights2 += d_weights2

    def train(self, iterations):
        for i in range(iterations):
            self.feed_forward()
            self.back_prop()
