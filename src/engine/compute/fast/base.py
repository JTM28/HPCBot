import numpy as np
from numba import njit




@njit('f8(f8, f8)')
def sub(x, y):
    """ :returns (x - y) """

    return x - y


@njit('f8(f8, f8)')
def mult(x, y):
    """ :returns (x * y) """

    return x * y


@njit('f8(f8, f8)')
def div(x, y):
    """ :returns (x / y) """

    return x / y


@njit('f8(f8, f8)')
def logdiv(x, y):
    """ :returns The natural log "ln" -> ln(x / y) """

    return np.log(x / y)


@njit("f8(f8[:])")
def cumsum(x):
    """ :returns The cumulative sum of an array """

    s = 0.0
    for i in np.arange(len(x)):
        s += x[i]

    return s



@njit('f8(f8[:])')
def meanavg(x):
    """ :returns The mean average of an array """
    s = cumsum(x)

    return s / len(x)


@njit("f8(f8[:])")
def stdev(x):
    """ :returns The standard deviation of an array """
    n = len(x)
    k = 1 / n
    avg = meanavg(x)
    dev = 0

    for i in range(len(x)):
        var = (x[i] - avg) ** 2
        mse = np.sqrt(var)
        dev += mse
    dev *= k
    return dev

