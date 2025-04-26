# Static method: a method that belongs to a class rather than any object from that
# class (instance). They don't use "self".
# They are usually used for general utility functions that do not need access to
# class data.

# Instance methods are best for operations on instances of the class (objects). They
# use "self".

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        """ Instance method """

        return f"\n{self.name} is a {self.position}"

    @staticmethod
    def is_valid_position(position):
        """ Static method: I don't have to rely on any object to use this
        method. """

        valid_positions = ['Manager', 'Cashier', 'Cook', 'Janitor']

        return position in valid_positions


def main() -> None:

    # To use a static method, I can use the class's name, instead of an instance
    # of the class:
    print(Employee.is_valid_position('Cook'))
    print(Employee.is_valid_position('Scientist'))

    employee1 = Employee('Mr Krabs', 'Manager')
    employee2 = Employee('Squidwards', 'Cashier')
    employee3 = Employee('Spongebob', 'Cook')

    print(employee1.get_info(), employee2.get_info(), employee3.get_info())


if __name__ == '__main__':
    main()
