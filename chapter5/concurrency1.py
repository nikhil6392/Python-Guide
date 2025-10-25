""" Concurrent features """

import concurrent.futures
import time

def worker(num):
    print(f'Worker {num} executing')
    time.sleep(1)
    return num

if __name__ == '__main__':

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(worker, i) for i in range(5)]

        for f in concurrent.futures.as_completed(results):
            print(f.result())


""" 
    Output : Worker 0 executing
             Worker 1 executing
             Worker 2 executing
             Worker 3 executing
             Worker 4 executing
             0
             1
             3
             4
             2       
"""