# A daemon thread is a thread that runs in the background, not important for
# the program to run. A program will not wait for daemon threads to complete
# before exiting.
# Non-daemon threads cannot normally be killed, they will stay alive unitil
# their task is complete.

# A few common uses of daemon threads: tasks, garbage collection, waiting for
# input, long-running processes...

import threading
import time


def timer():
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print(f"logged in for {count // 60} minutes and {count} seconds")


# x = threading.Thread(target=timer)
# x.start()
#
# answer = input("Do you wish to exit?  - ")

# When I try to exit this program, the main thread stops, but the background
# thread still works. The program will not exit as long as there is a non-daemon
# thread running.

# I have to transform the background thread to a daemon thread:

x = threading.Thread(target=timer, daemon=True)
x.start()

answer = input("Do you wish to exit?  - ")

# Now, when I enter some input, the main thread ends. That is the only non-daemon
# thread, so the program also exits.


print("\n-----------------------\n")


# I can also use the .setDaemon() method of a thread to change a thread to a
# non-daemon or daemon. If the thread is already running, I cannot change it.
# I have to use it before the .start() method.
# This method is currently deprecated in favor of the "daemon" attribute.

# I can check if a thread is a daemon:

print("Is this thread a daemon?", x.daemon)
