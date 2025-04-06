# Duck typing is the concept where the class of an object is less important
# than the methods / attributes the class may have.
# The class type is not checked if the minimum methods / attributes are present.

class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is qwacking")


class Chicken:

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")


class Person:

    def catch(self, duck):
        """ Both duck and chicken will satisfy the requirements for
        this method to work, even if it's intended for the duck. """

        duck.walk()
        duck.talk()
        print("You caught the animal!")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
print("------------")
person.catch(chicken)
