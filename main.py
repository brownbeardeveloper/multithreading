from concurrent.futures import ThreadPoolExecutor
from time import sleep
from threading import current_thread
import random

values = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
]


def task(x):
    thread_name = current_thread().name
    rnd_nbr = random.randint(0, 10)
    print(f"{thread_name} with value {x}: sleeping {rnd_nbr}s")
    sleep(rnd_nbr)
    return x * x * x


if __name__ == "__main__":
    result = []
    with ThreadPoolExecutor(max_workers=8) as exe:
        result = exe.map(task, values)

    for r in result:
        print(r)
