import time

print(time.time())

total = 0


def so_slow():
    for x in range(1, 10000):
        for y in range(1, 10000):
            total = x+y
    print(time.time())


so_slow()
