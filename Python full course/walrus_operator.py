# The walrus operator ( := ) assigns values to variables as part of a larger
# expression.

print(happy := True)
print(happy)

print("\n--------------------\n")

foods = []

while True:

    food = input("What food do you like?  - ")

    if food == "quit":
        break

    foods.append(food)

# Using the walrus operator:

while food := input("What food do you like?  - ") != "quit":
    foods.append(food)
