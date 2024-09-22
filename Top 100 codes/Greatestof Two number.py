# method 1 
def greatest(num1,num2):
    if num1 > num2:
        print(f"{num1} is the greatest number")
    else:
        print(f"{num2} is the greatest number")

greatest(40,50)
# method 2 using ternary operator 

num1, num2 = 20,30
print((num1 if num1 > num2 else num2))

#method 3 using max function
print(max(num1,num2))