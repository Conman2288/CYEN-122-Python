'''
# Sets
a = {1, 2, 3, 4, 5,}
b = {3, 4, 5, 6, 7}

# set operations
# Union
print(a | b)

# Intersection
print(a & b)


# Difference
print(a - b) # the elements in a that are not in b
'''

# Dictionary
# key-value pairs
# anything can be used as a key, as long as it is immutable (unchangable)
offices = {"Jones" : 247, "Smith" : 121, "Kennedy" : 108}
print(offices["Jones"])

# Remove a key-value pair
del offices["Jones"]

# Change a value
offices["Kennedy"] = 111

if ("Smith" in offices):
    print("Found Smith!")


# create a new key-value pair
offices[12345] = "howdy"

print(offices)

# Access just the keys
for k in offices.keys():
    print(offices[k])


# Acces the key-value pairs
for k, v in offices.items():
    print(k, "->", v)

# Dictionary comprehension
# write a dictionary comprehension wiht the valuess 1-5 as keys and their cubes as values
cubes = {x : x**3 for x in range(1,6)}
print(cubes)
