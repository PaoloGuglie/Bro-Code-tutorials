# Multiprocessing is the act of running tasks in paralled on different CPU cores
# by bypassing the GIL.
# It is better for tasks that are heavy CPU bound (heavy CPU usage)

from multiprocessing import Process
import time


def counter(number: int) -> None:
    count = 0
    while count < number:
        count += 1


def main():

    a = Process(target=counter, args=(100_000_000,))

    # Starting time
    starting_time = time.time()

    # Start the process
    a.start()

    # Important to add a process synchronization so that the main process waits
    # for the child process to finish before continuing
    a.join()

    # Finish time
    finish_time = time.time() - starting_time

    print(f"\nWith 1 process, I finished in {finish_time} seconds")


if __name__ == '__main__':

    # I need this in Windows because, when I run a program, I have a "main" process
    # that is running. If I create a child process from that process it's going
    # to copy the module that created it and the child process would create its own
    # children processes and so on...

    # By creating this, when I create a child process, it will copy the module, but
    # it will not execute it.

    main()
