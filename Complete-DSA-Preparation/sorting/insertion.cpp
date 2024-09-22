#include <bits/stdc++.h> // Include the standard library
using namespace std;     // Use the standard namespace

// Function to perform selection sort on an array
void insertion_sort(int arr[], int n)
{
    for (int i = 0; i <= n - 1; i++)
    {
        int j = i;
        while (j > 0 && arr[j - 1] > arr[j]){
            int temp = arr[j - 1];
            arr[j - 1] = arr[j];
            arr[j] = temp;
            j--;
        }
    }
}

int main()
{
    int n;
    cin >> n;   // Input the number of elements in the array
    int arr[n]; // Declare an array of size n
    // Input n elements into the array
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    // Call the selection sort function to sort the array
    insertion_sort(arr, n);
    // Output the sorted array
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    return 0; // Return 0 to indicate successful execution
}
