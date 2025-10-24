import multiprocessing

def worker(num):
    print(f'Worker {num} executing')
    return

if __name__ == '__main__':
    with multiprocessing.Pool(processes=5) as pool:
        pool.map(worker, range(5))