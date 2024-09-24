# Example
# Input : number = 123
# Output : 6
'''
#Method 1: simple approach
num = input("Enter Number: ")
sum = 0

for i in num:
    sum = sum + int(i)

print(sum)
'''
#Method 2

num = 123456

def findSum(num):
    if num == 0:
        return 0
    return int(num % 10) + findSum(num / 10)


print(findSum(num))


