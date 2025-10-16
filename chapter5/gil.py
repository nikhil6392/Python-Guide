"""Global Interpreter Lock(GIL)"""

import threading

x = 0

def increment():
    global x
    for i in range(1000000):
        x += 1

threads = []
for i in range(10):
    t = threading.Thread(target=increment)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print(x)