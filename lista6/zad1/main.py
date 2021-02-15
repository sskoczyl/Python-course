from neural_network import NeuralNetwork
import numpy as np
from functions import ReLU, Sigmoid


def print_values(v):
    for i in v:
        print(i, end=' ')
    print()


def run_tests(func1, func2, X, y):
    nn = NeuralNetwork(X, y, func1, func2)
    nn.train(5000)

    print("Kombinacja:", func1.__class__.__name__, " i", func2.__class__.__name__)
    print("Oczekiwane:", end=' ')
    print_values(y)
    print("Otrzymane: ", end=' ')
    print_values(nn.output)
    print('Błąd', np.linalg.norm(y - nn.output))
    print()


def main():
    """
        Ostatnia kolumna w X to bias. Umożliwia on nam "przesuniecie" aproksymowanej funkcji.
        Podobnie jak na poprzedniej liście przy regresjii liniowej (również dodawaliśmy kolumnę '1')

    """

    X = np.array([[0, 0, 1],
                  [0, 1, 1],
                  [1, 0, 1],
                  [1, 1, 1]])

    funs = [ReLU(), Sigmoid()]

    print('------------------------------------------')
    print("xor:")  # run test for xor
    y = np.array([[0], [1], [1], [0]])
    run_tests(funs[1], funs[1], X, y)
    run_tests(funs[0], funs[1], X, y)
    run_tests(funs[1], funs[0], X, y)
    run_tests(funs[0], funs[0], X, y)
    print('------------------------------------------')
    print("and:")  # and
    y = np.array([[0], [0], [0], [1]])
    run_tests(funs[1], funs[1], X, y)
    run_tests(funs[0], funs[1], X, y)
    run_tests(funs[1], funs[0], X, y)
    run_tests(funs[0], funs[0], X, y)
    print('------------------------------------------')
    print("or:")  # or
    y = np.array([[0], [1], [1], [1]])
    run_tests(funs[1], funs[1], X, y)
    run_tests(funs[0], funs[1], X, y)
    run_tests(funs[1], funs[0], X, y)
    run_tests(funs[0], funs[0], X, y)
    print('------------------------------------------')


if __name__ == '__main__':
    main()
