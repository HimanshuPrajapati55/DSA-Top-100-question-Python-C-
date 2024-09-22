# Problem : Sum of First N natural number

def sum_of_nautral_number(n):
    product = 0
    if n < 0:
          print("enter a valid number")
    elif n == 0:
         print(product) 
    else:
         for i in range(1,n+1):
              product += i
    
    print(product)
    
    
# without using for loop 

def getSum(num):
    if num == 1:
        return 1
    return num + getSum(num-1) 

number = int(input("Enter a Valid Natural number"))
sum_of_nautral_number(n = number)
print(getSum(num = number))

# Method 3 using formula
print(int(number*(number+1)/2))
