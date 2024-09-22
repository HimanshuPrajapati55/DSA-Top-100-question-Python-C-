def great(num1,num2,num3):
    if num1 > num2 and num1>num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3
    
print(great(10,50,40))
print(great(4,2,1))
print(great(101,102,200))