from neural_network import NeuralNetwork
import numpy as np
from functions import ReLU, Sigmoid, Tanh
import matplotlib.pyplot as plt


def learn_sinus(x_input, y_expected, X_testing):
    x_chng, y_chng = np.reshape(x_input, (len(x_input), 1)), np.reshape(y_expected, (len(y_expected), 1))
    X_chng = np.reshape(X_testing, (len(X_testing), 1))
    nn = NeuralNetwork(x_chng, y_chng, Sigmoid(), Tanh(), 0.5)

    plot_learn = plt.figure()
    sub1, sub2 = plot_learn.add_subplot(2, 1, 1), plot_learn.add_subplot(2, 1, 2)
    sub1.scatter(x_input, y_expected)

    for i in range(100):
        nn.train(1000)
        nn.input = X_chng
        nn.feed_forward()

        sub2.clear()
        sub2.set_xlabel(str(i) + 'k')
        sub2.scatter(X_chng, nn.output.flatten())

        nn.input = x_chng
        plt.pause(0.0001)
    plt.show()


def learn_paraola(x_input, y_expected, X_testing):
    x_chng, y_chng = np.reshape(x_input, (len(x_input), 1)), np.reshape(y_expected, (len(y_expected), 1))
    X_chng = np.reshape(X_testing, (len(X_testing), 1))
    nn = NeuralNetwork(x_chng, y_chng, Sigmoid(), Sigmoid(), 0.5)

    plot_learn = plt.figure()
    sub1, sub2 = plot_learn.add_subplot(2, 1, 1), plot_learn.add_subplot(2, 1, 2)
    sub1.scatter(x_input, y_expected)

    for i in range(100):
        nn.train(1000)
        nn.input = X_chng
        nn.feed_forward()

        sub2.clear()
        sub2.set_xlabel(str(i) + 'k')
        sub2.scatter(X_chng, nn.output.flatten())

        nn.input = x_chng
        plt.pause(0.0001)
    plt.show()


def main():
    x_input = np.linspace(-50, 50, 26)
    x_input = x_input / max(x_input)
    y_expected = x_input ** 2

    X_testing = np.linspace(-50, 50, 101)
    X_testing = X_testing / max(X_testing)

    learn_paraola(x_input, y_expected, X_testing)

    x_input = np.linspace(0, 2, 21)
    y_expected = np.sin(x_input * (3 * np.pi / 2))
    X_testing = np.linspace(0, 2, 101)
    X_testing = X_testing / max(X_testing)

    learn_sinus(x_input, y_expected, X_testing)


if __name__ == '__main__':
    main()
