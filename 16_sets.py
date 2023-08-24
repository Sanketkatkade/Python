# a = {1, 2, 3, 4, 1}
# print(type(a))
# print(a)

# This will create an empty dictionary not and empty set
# b = {}
# print(type(b))

# This will create an empty set
c = set()
print(type(c))

c.add(3)
c.add(2)
c.add(8)
c.add(5)
c.add(3) # it will not add these 3 because 3 is already added in the set 
# c.add([4, 5, 6]) # we can't add list in the set
c.add((4, 5, 6)) # we can't add dictionary in the set
# print(c)
# print(len(c))
c.remove((4, 5, 6))
# c.remove(15) # It will throw an error because 15 is not present in the set
print(c)
print(c.pop())
print(c)
print(len(c))

# c.clear() # Ir will clear the set
# print(c)



