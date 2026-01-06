// INHERITANCE

#include <iostream>
using namespace std;
using str = std::string;

class Animal
{
    public:
        bool alive = true;
    
        void eat() {
            cout << "This animal is eating." << endl;
        }
};

class Dog : public Animal
{
    public:
        void bark() {
            cout << "The dog barks!" << endl;
        }
};

class Cat : public Animal
{
    public:
        void meow() {
            cout << "The cat meows!" << endl;
        }
};

int main()
{
    Dog dog;
    dog.eat();
    dog.bark();

    Cat cat;
    cat.eat();
    cat.meow();

    return 0;
}