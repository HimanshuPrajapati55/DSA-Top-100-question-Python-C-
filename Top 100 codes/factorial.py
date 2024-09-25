num = 5
fact = 1

if num < 0:
    print("Enter a valid number")
else:
    for i in range(1,num+1):
        fact = fact * i
    
print("factorial of",num, "is", fact)

# Method 2
def getfactorial(num1):
    if num1 == 0:
        return 1
    
    return num1 * getfactorial(num1 - 1)

num1 = 6
print(getfactorial(num1))