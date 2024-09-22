#include <bits/stdc++.h>  // Include the standard library
using namespace std;

void bubble_sort(int arr[],int n){
    for(int i=n-1;i>=0;i--){
        int didSwap = 0;
        for(int j=0;j<=i-1;j++){
            if(arr[j]>arr[j+1]){
                int temp = arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = temp;
                didSwap = 1;
            }

        }
        if(didSwap == 0){
            break;
        }
    }
}

int main() {
    int n;
    cin >> n;  // Input the number of elements in the array
    int arr[n];  // Declare an array of size n
    // Input n elements into the array
    for (int i = 0; i < n; i++) cin >> arr[i];
    // Call the selection sort function to sort the array
    bubble_sort(arr, n);
    // Output the sorted array
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    return 0;  // Return 0 to indicate successful execution
}