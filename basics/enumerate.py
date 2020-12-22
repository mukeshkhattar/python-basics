grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery)) # <class 'enumerate'>

# converting to list
print(list(enumerateGrocery)) # [(0, 'bread'), (1, 'milk'), (2, 'butter')]

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery)) # [(10, 'bread'), (11, 'milk'), (12, 'butter')]
