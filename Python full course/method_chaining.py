# Method chaining: calling multiple methods squentially. Each call
# performs an action on the same object and returns "self".


class Car:
    """ Each method used in method chaining has to return "self" so
    that I can call them sequentially. Without that, when I call the
     first method in the chain, it returns None, and I cannot apply
     any further method of the chain. """

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self


car = Car()

car.turn_on().drive().brake().turn_off()

print("-------")


# I can refractor the code with the line continuation character "\":

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()

print("-------")


# Or with parentheses:

(car.turn_on()
 .drive()
 .brake()
 .turn_off())
