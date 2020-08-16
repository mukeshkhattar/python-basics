
# This program shows various identities
str1 = "geek"
print(id(str1)) # 4318823344
print(id("geek")) # 4318823344

str2 = "geek"
print(id(str2)) # 4318823344

# This will return True
print(id(str1) == id(str2))

str2 = "geek1"
print(id(str2)) # 4318823280

# Use in Lists
list1 = ["geek", "geek1", "abdul"]
print(id(list1[0])) # 4318823344
print(id(list1[1])) # 4318823280

