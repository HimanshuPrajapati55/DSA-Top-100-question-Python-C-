def equivalent_positive_index(s, k):
    n = len(s)
    if -n <= k < 0:
        return n + k
    else:
        raise ValueError("Index out of range")

# Test the function
s = "hello"
negative_indices = [-1, -2, -3, -4, -5]

for k in negative_indices:
    j = equivalent_positive_index(s, k)
    print(f"s[{k}] is equivalent to s[{j}] which is '{s[j]}'")
