# question power of number

# Method 1: using pow() function
num1, power1 = 3,2
print(pow(num1,power1))

#Method 2: Simple  iteration

num,power = 2, 3
output = 1
for i in range(power):
    output *= num
print(output)

# MEthod  3
num, power = 3, 2
print(num**power)

# Method 4 using recusriosn

num4, power4 = 2, 3
def power12(num4,power4):
    if power4 == 0:
        return 1
    return num4 * power12(num,power4 - 1)
print(power12(num4, power4))