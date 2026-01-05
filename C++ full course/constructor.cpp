// A CONSTRUCTOR is a special method automatically
// called when an object is instantiated.
// It's useful for assigning values to attributes
// as arguments.

#include <iostream>

using namespace std;
using str = std::string;

class Student
{
    public:
        str name;
        int age;
        double gpa;
    
    // CONSTRUCTOR
    Student(str name, int age, double gpa) {
        this->name = name;
        this->age = age;
        this->gpa = gpa;
    }
};

int main()
{
    Student guy("Jack", 25, 4.0);
}