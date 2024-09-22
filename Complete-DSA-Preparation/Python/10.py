# rite a pseudo-code description of a function that reverses a list of n
# integers, so that the numbers are listed in the opposite order than they
# were before, and compare this method to an equivalent Python function
# for doing the same thing.

def rev(data):
    start = 0
    end = len(data) - 1

    while start<end:
        data[start],data[end] = data[end],data[start]

        start +=1
        end-=1
    return data


data = [1,2,3]
print(rev(data))