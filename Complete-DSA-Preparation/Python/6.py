def squ(n):
    if(n<=0):
        return ValueError("input must be positive")
    
    total = 0
    
    for i in range(1,n):
        if(i%2==1):
            total += i*i

    
    return sum([i * i for i in range(1,n) if i%2 == 1])


print(squ(n=5))
