// Dynamic allocated memory is in the heap.
// use keyword "new" to allocate space. It returns
// a pointer to the allocated memory.

#include <iostream>

int main()
{
    int *pnum = NULL;

    pnum = new int;  // this is like malloc(sizeof(int));

    delete pnum;  // free the memory at the address, like free();
}

int main()
{
    char *pgrades = NULL;

    pgrades = new char[5];  // allocate an array of 5 char values.

    delete pgrades;
}

int main()
{
    char *pgrades = NULL;
    int size;

    std::cout << "How many grades?  - ";
    std::cin >> size;

    pgrades = new char[size];

    delete pgrades;
}