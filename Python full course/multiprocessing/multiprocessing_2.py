# I can speed up the previous's file code

from multiprocessing import Process, cpu_count
from time import time


def counter(number):
    count = 0
    while count < number:
        count += 1


def main():

    # Divide the count to 100_000_000 in half for each process:
    a = Process(target=counter, args=(50_000_000,))
    b = Process(target=counter, args=(50_000_000,))

    starting_time = time()

    a.start()
    b.start()

    a.join()
    b.join()

    finish_time = time() - starting_time

    print(f"\nWith 2 processes, I finished in {finish_time} seconds")


if __name__ == '__main__':
    main()
