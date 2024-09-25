def fibo(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibo(i-1) + fibo(i-2)

num = 10
if num <= 0 :
    print("enter a positive number")
else:
    print("Fibonacci series:",end = " ")

for i in range(num):
    print(fibo(i), end = " ")

