import numpy as np

class Perceptron(object):

    def __init__(self, w, threshold):
        self.w = w
        self.threshold = threshold

    def predict(self, x):
        val = np.sum(self.w*x)
        return 0 if val <= self.threshold else 1

if __name__ == '__main__':
    size = 10
    threshold = 0.25*size

    n_zeros, n_ones = 0, 0
    for i in range(100):
        w = np.random.rand(size)
        x = np.random.rand(size)

        perceptron = Perceptron(w, threshold)
        result = perceptron.predict(x)
        n_ones = n_ones + result
        n_zeros = n_zeros + (1-result)

    print("{0} zeros and {1} ones.".format(n_zeros, n_ones))
