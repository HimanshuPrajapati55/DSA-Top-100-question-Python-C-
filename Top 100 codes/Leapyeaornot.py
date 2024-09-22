def leapyear(year):
    if (year % 4 == 0 and year%100 != 0) or year % 400 == 0:
        return "leap year"
    else :
        return "not leap year"

print(leapyear(2023))