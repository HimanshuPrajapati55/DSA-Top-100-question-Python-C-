import random

def custom_shuffle(data):
    n = len(data)
    for i in range(n-1, 0, -1):
        j = random.randint(0, i)  # Generate a random index from 0 to i
        data[i], data[j] = data[j], data[i]  # Swap elements

# Example usage:
data = [1, 2, 3, 4, 5]
custom_shuffle(data)
print(data)
