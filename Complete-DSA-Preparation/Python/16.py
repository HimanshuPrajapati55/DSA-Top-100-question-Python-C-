def dot_product(a,b):
    if len(a) != len(b):
        raise ValueError("The array Must be same length")
    n = len(a)
    c = [0]*n

    for i in range(n):
        c[i] = a[i]*b[i]

    return c

a = [1,2,3,4]
b = [5,6,7,8]

result = dot_product(a,b)
print(result)