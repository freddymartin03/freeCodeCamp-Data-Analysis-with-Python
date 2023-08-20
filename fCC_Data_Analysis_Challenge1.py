import numpy as np


def calculate(lst):
    if len(lst) != 9:
        raise ValueError('List must contain nine numbers.')

    np_array = np.array(lst)
    matrix = np_array.reshape(3, 3)
    print(matrix)

    mean = [list(matrix.mean(axis=0)), list(matrix.mean(axis=1)), matrix.mean()]
    variance = [list(matrix.var(axis=0)), list(matrix.var(axis=1)), matrix.var()]
    standard_deviation = [list(matrix.std(axis=0)), list(matrix.std(axis=1)), matrix.std()]
    maximum = [list(matrix.max(axis=0)), list(matrix.max(axis=1)), matrix.max()]
    minimum = [list(matrix.min(axis=0)), list(matrix.min(axis=1)), matrix.min()]
    tot_sum = [list(matrix.sum(axis=0)), list(matrix.sum(axis=1)), matrix.sum()]

    calculations = {
        'mean': mean, 'variance': variance, 'standard deviation': standard_deviation, 'max': maximum, 'min': minimum,
        'sum': tot_sum
    }

    return calculations