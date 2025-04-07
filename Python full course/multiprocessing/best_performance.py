from multiprocessing import Process, cpu_count
from time import time

MAX_PROCESSES = cpu_count()


def counter(number):
    count = 0
    while count < number:
        count += 1


def main():

    processes = []

    starting_time = time()

    for _ in range(MAX_PROCESSES):
        i = Process(target=counter, args=(1_000_000,))
        processes.append(i)
        i.start()

    for i in processes:
        i.join()

    finish_time = time() - starting_time

    print(f"\nWith {MAX_PROCESSES} processes, I finished in {finish_time} seconds")


if __name__ == '__main__':
    main()
