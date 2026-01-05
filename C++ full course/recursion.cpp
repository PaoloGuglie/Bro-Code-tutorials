// RECURSION is a programming techinique where
// a function invokes itself from within.
 
// advantages compared to ITERATIVE approach:
//  - less code and cleaner
//  - useful for sorting and searching algorithms

// disadvantages:
//  - uses more memory
//  - slower

// Recursion can cause STACK OVERFLOW because, when I
// invoke a function, I add a frame to the stack.


#include <iostream>

void walk(int);

int main()
{
    walk(10);

    return 0;
}

void walk(int steps)
{
    if (steps > 0)
    {
        std::cout << "You take a step!" << std::endl;

        walk(steps - 1);
    }
}