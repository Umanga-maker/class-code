import numpy as np
N = 100_000_000
def sum_python():
    return sum(range(N))

def sum_numpy():
    return np.sum(np.arange(N))

print(sum_python())
print(sum_numpy())

import timeit
print("sum python:", timeit.timeit(sum_python, number=1))
print("sum numpy:", timeit.timeit(sum_numpy, number=1))
