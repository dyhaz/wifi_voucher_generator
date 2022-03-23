# generate random Gaussian values
from random import seed
from random import gauss

# seed random number generator
seed(69)


def randomize(digits=10):
    values = []

    # generate some Gaussian values
    for _ in range(20):
        value = str(gauss(0, 1)).split('.')[1][0:digits]
        values.append(value)
    return values
