// A FUNCTION TEMPLATE describes what a function
// look like.
// It can be used to generate as many overloaded
// functions as needed, each using different data types.

#include <iostream>

template <typename T>

T max(T x, T y)
{
    return (x > y) ? x : y;
}

int main()
{
    std::cout << max(2, 5) << std::endl;
    std::cout << max(1.2, 1.1) << std::endl;
    std::cout << max('a', 'A') << std::endl;

    return 0;
}

// I have a problem: right now, max() does not accept arguments of
// different types (the template has only type T).
// Here's what I can do:

template <typename T, typename U>

auto max(T x, U y)
{
    return (x > y) ? x : y;
}

// (I can also do T max(U x, T y) )
// Using the "auto" keyword, the compiler deduces the return type,
// otherwise it matches the T type, which could troncate y if
// y was a float and x an int.