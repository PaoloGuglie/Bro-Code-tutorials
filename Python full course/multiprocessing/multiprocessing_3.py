# I can speed up the previous's file code

from multiprocessing import Process, cpu_count
from time import time


def counter(number):
    count = 0
    while count < number:
        count += 1


def main():

    print(f"I can run up to {cpu_count()} processes.")

    # Divide the count to 100_000_000 in a quarter for each process:
    a = Process(target=counter, args=(25_000_000,))
    b = Process(target=counter, args=(25_000_000,))
    c = Process(target=counter, args=(25_000_000,))
    d = Process(target=counter, args=(25_000_000,))

    starting_time = time()

    a.start(); b.start(); c.start(); d.start()

    a.join(); b.join(); c.join(); d.join()

    finish_time = time() - starting_time

    print(f"\nWith 4 processes, I finished in {finish_time} seconds")

    # If I run more processes than the ones my CPU can handle (to know
    # the number of processes available use the function cpu_count()),
    # I will slow down my program.


if __name__ == '__main__':
    main()
