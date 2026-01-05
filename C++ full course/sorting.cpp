#include <iostream>

using namespace std;

using str = std::string;

void sort(int [], int);

int main()
{
    int arr[] = {20, 1, 40, 5, 8, 3};
    int size = sizeof (arr) / sizeof (int);

    cout << "Unsorted array:" << endl;
    for (int i : arr)
    {
        cout << i << " ";
    }
    cout << endl;

    sort(arr, size);

    cout << "Sorted array:" << endl;
    for (int i : arr)
    {
        cout << i << " ";
    }
    cout << endl;

    return 0;
}

// Bubble sort
void sort(int arr[], int size)
{
    int temp;

    for (int i = 0; i < size - 1; i++)
    {
        for (int j = 0; j < size -i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}