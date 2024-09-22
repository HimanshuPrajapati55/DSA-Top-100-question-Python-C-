def check_formula(a,b,c):
    if a+b == c:
        return f"{a} + {b} = {c} is a valid formula."
    elif a== b-c:
        return f"{a} + {b} = {c} is a valid formula."
    elif a * b == c:
        return f"{a} + {b} = {c} is a valid formula."
    

a = int(input("Enter the first integer (a): "))
b = int(input("Enter the second integer (b): "))
c = int(input("Enter the third integer (c): "))

# Check for a valid arithmetic formula
result = check_formula(a, b, c)
print(result)