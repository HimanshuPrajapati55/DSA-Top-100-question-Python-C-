#include <bits/stdc++.h>  // Include the standard library
using namespace std;  // Use the standard namespace

// Function to perform selection sort on an array
void selection_sort(int arr[], int n) {
    // Loop over the array to find the minimum element in the unsorted part
    for (int i = 0; i <= n - 2; i++) {
        int mini = i;  // Initialize mini to the current position i
        // Find the minimum element in the unsorted part of the array
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[mini]) {  // Compare current element with the minimum
                mini = j;  // Update mini if a smaller element is found
            }
        }
        // Swap the found minimum element with the first element of the unsorted part
        int temp = arr[mini];
        arr[mini] = arr[i];
        arr[i] = temp;
    }
}

int main() {
    int n;
    cin >> n;  // Input the number of elements in the array
    int arr[n];  // Declare an array of size n
    // Input n elements into the array
    for (int i = 0; i < n; i++) cin >> arr[i];
    // Call the selection sort function to sort the array
    selection_sort(arr, n);
    // Output the sorted array
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    return 0;  // Return 0 to indicate successful execution
}
