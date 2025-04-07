# A thread is a flow of execution. Each thread can carry its own separate
# order of instructions.
# MULTITHREADING can have the program run different parts at the same time. They
# all run concurrenly but not in parallel (that would be MULTIPROCESSING).

# Each thread takes a turn running to achieve concurrency. This is due to a
# feature called the Global Interpreter Lock (GIL): only one thread can run,
# taking control of the Python interpreter, at one time, but they can take turns
# when one thread is idle.


# Programs and tasks can be divided in two different categories:

#   - CPU bound: program or task that spends most of it's time waiting for
#     internal events (CPU intensive).
#     Better to use MULTIPROCESSING for tasks that are CPU bound.

#   - I/O bound: program or task that spends most of it's time waiting for
#     external events (user input, web scraping...)
#     Better to use MULTITHREADING: multiple threads running concurrenly, but
#     not trully in parallel.

import threading
import time

print("-----------------------\n")

# I can count the number of threads that are currently running in the background.
# Whenever I run a program, I have one thread that is running in charge of executing
# my program:
print(threading.active_count())  # I should have 1 thread active now.
print("----------")
print(threading.enumerate())  # The "MainThread"


print("\n-----------------------\n")


# Sequential code:

def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast.")


def drink_coffee():
    time.sleep(4)
    print("You drank coffee.")


def study():
    time.sleep(5)
    print("You finished studying.")


starting_time = time.time()

eat_breakfast(); drink_coffee(); study()

print(f"\nThis SEQUENTIAL code took {int(time.time() - starting_time)} seconds to run")


print("\n-----------------------\n")


# Concurrent code (create three other threads while the main thread runs in
# the background to complete the rest of the program):

def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast.")


def drink_coffee():
    time.sleep(4)
    print("You drank coffee.")


def study():
    time.sleep(5)
    print("You finished studying.")


starting_time = time.time()

x = threading.Thread(target=eat_breakfast, args=())

y = threading.Thread(target=drink_coffee, args=())

z = threading.Thread(target=study, args=())

# Start threads
x.start()
y.start()
z.start()

# To make the main thread wait for all the other threads to finish before
# printing the last line, I can use thread synchronization:
x.join()
y.join()
z.join()

# Without the .join() method, the main thread will finish counting time without
# waiting for the threads to end by immediately printing the last line right
# after creating the threads.

print(f"\nThis CONCURRENT code took {int(time.time() - starting_time)} seconds to run")
