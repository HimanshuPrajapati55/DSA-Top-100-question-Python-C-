# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

# Generate the list using list comprehension
result = [n * (n + 1) for n in range(10)]

# Display the result
print(result)

# Generate the list of lowercase letters using list comprehension
alphabet = [chr(i) for i in range(97, 123)]

# Display the result
print(alphabet)  # Expected output: ['a', 'b', 'c', ..., 'z']
