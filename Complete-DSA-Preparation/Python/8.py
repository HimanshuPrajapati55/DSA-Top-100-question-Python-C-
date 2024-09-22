# What parameters should be sent to the range constructor, to produce a
# range with values 50, 60, 70, 80?

r = range(50,90,10)
p = range(8,-10,-2)
print(list(r))
print(list(p))

#  Demonstrate how to use Python’s list comprehension syntax to produce
# the list [1, 2, 4, 8, 16, 32, 64, 128, 256].

powers_of_2 = [2**i for i in range(9)]
print(powers_of_2)