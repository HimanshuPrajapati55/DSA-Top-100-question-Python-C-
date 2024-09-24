import math

def prime_range(start, end):
    prime = []
    if end < start:
        return "Not a Valid Range"
    
    for i in range(start, end + 1):
        if i < 2:
            continue 
        if i == 2:
            prime.append(2)
            continue
        
        flag = 0
        for x in range(2, int(math.sqrt(i)) + 1):  # Optimized divisor check
            if i % x == 0:
                flag = 1
                break

        if flag == 0:
            prime.append(i)

    return prime

print(prime_range(2, 10))
