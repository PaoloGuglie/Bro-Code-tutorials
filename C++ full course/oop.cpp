#include <iostream>

class Human
{
    public:
        std::string name = "nemo";
        std::string occupation = "unemployed";
        int age = 0;

        void present() {
            std::cout << "This person's name is " << name << std::endl;
            std::cout << "This person's job is " << occupation << std::endl;
            std::cout << "This person's age is " << age << std::endl;
        }

        void eat() {
            std::cout << "This person is eating" << std::endl;
        }

        void drink() {
            std::cout << "This person is drinking" << std::endl;
        }

        void sleep() {
            std::cout << "This person is sleeping" << std::endl;
        }
};

int main()
{
    Human guy;
    guy.name = "Rick";
    guy.occupation = "Scientist";
    guy.age = 70;

    guy.present();

    guy.drink();

    Human other;
    other.present();

    return 0;
}