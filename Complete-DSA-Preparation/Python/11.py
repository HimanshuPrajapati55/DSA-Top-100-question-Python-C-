def has_odd_product_pair(seq):
    # Find all odd numbers in the sequence
    odd_numbers = [num for num in seq if num % 2 != 0]
    
    # Check if there are at least two odd numbers
    return len(odd_numbers) >= 2

# Test cases
print(has_odd_product_pair([1, 2, 3, 4, 5]))  # Expected output: True (1 and 3, or 1 and 5, etc.)
print(has_odd_product_pair([2, 4, 6, 8]))     # Expected output: False (no odd numbers)
print(has_odd_product_pair([1, 3, 5]))        # Expected output: True (1 and 3, or 1 and 5, etc.)
print(has_odd_product_pair([1, 2, 4, 6, 8, 10, 11]))  # Expected output: True (1 and 11)
print(has_odd_product_pair([2, 4, 6, 8, 10]))  # Expected output: False (no odd numbers)
