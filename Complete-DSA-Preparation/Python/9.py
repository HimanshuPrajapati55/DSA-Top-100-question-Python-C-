import random 

def choice(data):
    if not data:
        raise IndexError
    
    length = len(data)
    random_index = random.randrange(length)
    return data[random_index]

data = [10,20,30,40,50]
print(choice(data))
