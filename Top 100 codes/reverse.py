num = 12345
temp = num
reverse = 0
while num > 0:
    remainder = num%10 
    reverse = (reverse * 10) + remainder
    num = num // 10

print(reverse)

# Method 2 using recursion 

def recur(number, reve):
    if number == 0:
        return reve
    remainder = int(number % 10)
    reve = (reve*10)+ remainder
    return recur(int(number/10),reve)

num1 = 123
reve = 0 
print(recur(num1,reve))