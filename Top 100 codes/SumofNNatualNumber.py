def recursum(number):
    if number == 0:
        return number
    return number + recursum(number - 1)

number= 6
print(recursum(number))