// Passing a value by reference (new C++ feature)
// a reference (&) is a memory address
// use instead of pointers

// Pass by reference as often by possible unless I have
// a reason to pass by value

#include <iostream>

using namespace std;
using str = std::string;

void swap(str &, str &);  // REFERENCE

int main()
{
    str x = "Man";
    str y = "Woman";

    cout << "x was " << x << endl;
    cout << "y was " << y << endl;

    cout << '\n';

    swap(x, y);

    cout << "x is now " << x << endl;
    cout << "y is now " << y << endl;

    return 0;
}

// REFERENCE
void swap(str &a, str &b)
{
    str temp = a;

    a = b;
    b = temp;
}