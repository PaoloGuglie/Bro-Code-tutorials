# reduce() applies a function of my choosing to an iterable and redute it to
# a single cumulative value.
# It performs the function on the first two elements and repeats the process
# until 1 value remains.

import functools

print("-------------------\n")

letters = [i for i in 'Hello']
print(letters, "\n")

word = functools.reduce(lambda x, y: x + y, letters)

print("Union of words:", word)

print("\n-------------------\n")

factorial = [i for i in range(5, 0, -1)]
print(factorial, "\n")

result = functools.reduce(lambda x, y: x * y, factorial)
print("Factorial of 5:", result)
