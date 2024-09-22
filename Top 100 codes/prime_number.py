def prime_number(num):
    if num < 2:
        return "Not a Prime number"
    if num == 2:
        return "Prime Number" 
    for i in range(2,num):
        if num%i == 0:
            return "Not A prime number"
        return "Prime Number"
        
print(prime_number(11))