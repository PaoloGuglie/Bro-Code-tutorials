// GETTERS & SETTERS:
// Getters are functions that make a private attribute
// readable.
// Setters are functions that make a private attribute
// writeable.

#include <iostream>

using str = std::string;

class Stove
{
    private:
        int temperature = 0;
    
    public:
        int get_temp()
        {
            return this->temperature;
        }
        void set_temp(int n)
        {
            if (n < 0) this->temperature = 0;
            else if (n > 60) this->temperature = 60;
            else this->temperature = n;
        }
        void display_temp()
        {
            std::cout << "Temperature is " << this->get_temp()
            << " degrees." << std::endl;
        }
};

int main()
{
    Stove stove;

    stove.set_temp(40);
    stove.display_temp();

    stove.set_temp(-20);
    stove.display_temp();

    stove.set_temp(539);
    stove.display_temp();

    return 0;
}