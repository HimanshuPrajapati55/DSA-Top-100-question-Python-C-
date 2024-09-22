def squ(n):
    if(n<=0):
        return ValueError("input must be positive")
    
    total = 0
    for i in range(1,n):
        total += i*i

    return total


print(squ(n=5))
