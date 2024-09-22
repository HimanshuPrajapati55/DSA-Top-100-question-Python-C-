#  Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).
def dis(data):
    return len(data) == len(set(data))
    

data = [1,2,3,5]
print(dis(data))