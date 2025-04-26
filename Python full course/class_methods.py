# Class methods allow operations related to the class itself. They take "cls" as
# the first parameter, which represents the class itself.
# They are best for class-level data.

class Student:

    # Class variables:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        """ Whenever I create a Student object, the count is increased by 1 """

        self.name = name
        self.gpa = gpa

        # To access the class variables, I use the ClassName:
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        """ Instance method (has "self" as first parameter) """

        return f"{self.name} has a {self.gpa} gpa."

    @classmethod
    def get_count(cls):
        """ Class method (has "cls" as first parameter).
        To access class variables, I use "cls" instead of the
        ClassName. """

        return f"\nTotal number of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):

        try:
            avg_gpa = round(cls.total_gpa / cls.count, 1)

        except ZeroDivisionError:
            avg_gpa = 0

        return f'\nAverage gpa: {avg_gpa}'


def main() -> None:

    print(Student.get_count())
    print(Student.get_average_gpa())

    print("\n----------------------------")

    student1, student2, student3 = [Student(name, gpa) for name, gpa in
                                    zip(['Spongebob', 'Patrick', 'Sandy'], [3.2, 2.0, 4.0])]

    print(Student.get_count())
    print(Student.get_average_gpa())


if __name__ == '__main__':
    main()
