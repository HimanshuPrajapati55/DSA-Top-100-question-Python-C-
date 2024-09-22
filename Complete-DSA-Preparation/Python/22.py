def generate_permutations(chars):
    def permute(chars, l, r):
        if l == r:
            print(''.join(chars))
        else:
            for i in range(l, r + 1):
                # Swap the current index with the loop index
                chars[l], chars[i] = chars[i], chars[l]
                # Recurse on the rest of the characters
                permute(chars, l + 1, r)
                # Backtrack by swapping the characters back
                chars[l], chars[i] = chars[i], chars[l]

    permute(chars, 0, len(chars) - 1)

# List of characters to use
chars = ['c', 'a', 't', 'd', 'o', 'g']

# Generate and print all permutations
generate_permutations(chars)
