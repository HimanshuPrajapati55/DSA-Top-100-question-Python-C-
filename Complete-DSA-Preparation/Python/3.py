def minmax(data):
    if len(data)==0:
        return ValueError("Must contain atleast one number")
    
    smallest = largest = data[0]
    for num in data:
        if num<smallest:
            smallest = num
        if num>largest:
            largest = num

    return(smallest,largest)

print(minmax([3, 1, 4, 1, 5, 9, 2, 6, 5]))  # Expected output: (1, 9)
print(minmax([-10, -20, -30, -40, -50]))     # Expected output: (-50, -10)

