"""
ive a single command that computes the sum from Exercise R-1.4, relying 
on Python’s comprehension syntax and the built-in sum function.
"""

def squ(n):
    if(n<=0):
        return ValueError("input must be positive")
    
    return sum([i * i for i in range(1,n)])


print(squ(n=6))
