"""Processes for CPU-bound tasks"""

"""Processes can be used to improve the performance of CPU-bound tasks."""

from multiprocessing import Pool


def square(x):
    return x * x

if __name__ == '__main__':
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    with Pool() as pool:
        results = pool.map(square, numbers)
        print(results)
