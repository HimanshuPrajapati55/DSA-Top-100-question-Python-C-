# In Section 1.8, we provided three different implementations of a generator
# that computes factors of a given integer. The third of those implementations, from page 41, was the most efficient, but we noted that it did not
# yield the factors in increasing order. Modify the generator so that it reports
# factors in increasing order, while maintaining its general performance advantages.
def factors(n):
    small_factors = []
    large_factors = []
    
    k = 1
    while k * k <= n:
        if n % k == 0:
            small_factors.append(k)
            if k != n // k:
                large_factors.append(n // k)
        k += 1
    
    for factor in small_factors:
        yield factor
    for factor in reversed(large_factors):
        yield factor

# Example usage
n = 100
print(f"Factors of {n} in increasing order:")
for factor in factors(n):
    print(factor)
