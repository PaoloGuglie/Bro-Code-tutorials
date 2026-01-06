// OVERLOADED CONSTRUCTORS : multiple constructors with
// the same name but different parameters.
// They allow for a varying number of arguments when
// instantiating an object.

#include <iostream>

using str = std::string;

class Pizza
{
    public:
        str topping1;
        str topping2;

    // CONSTRUCTORS
    Pizza(str a) {
        this->topping1 = a;
    }
    Pizza (str a, str b) {
        this->topping1 = a;
        this->topping2 = b;
    }
    Pizza() {}
};

int main()
{
    Pizza pizza1("pepperoni");
    Pizza pizza2("cheese", "mushrooms");
    Pizza pizza3;

    return 0;
}