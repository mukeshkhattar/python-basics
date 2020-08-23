items=[2,3,4,5,6,7,8,9,10]
items2=items

print(hex(id(items)), hex(id(items2)))

#insert at 0th position
items.insert(0,1)

# append
items.append(11)

# pop removes the last item and returns it
x=items.pop()
print(x, type(x))
print(items) # 10 items values :1 -10

# update
# items[10]=11 >> error out of range
items[1]=2
items[1]=1
print(items)

#delete an item given index
del items[1]
print(items) # 1,3,4,...10
items.insert(1,2)
print(items) # 1,2,3,4,...10

#delete an item given value : first occurance only
items=['a','v','c','v','g','v','k','v']
items.remove('v')
print('remove:', items) #['a', 'c', 'v', 'g', 'v', 'k', 'v']


#search, raises ValueError if item is not found
items=['a','v','c','v','g','v','k','v']
x=items.index('v')
print(x) # 1
x=items.index('v',x+1)
print(x) # 3
x=items.index('v',x+1)
print(x) # 5
x=items.index('v',x+1)
print(x) # 7
# x=items.index('v',x+1)>>  ValueError


#sort the list in asc oreder
items.sort()
print(items) #['a', 'c', 'g', 'k', 'v', 'v', 'v', 'v']

#sort the list in desc oreder
items=['a','b','c','d','g','x','k','v']
items.sort(reverse=True)
print('sort in reverse:',items) # ['x', 'v', 'k', 'g', 'd', 'c', 'b', 'a']

#sort vs sorted
list1=[2,1,4,3]
print('sorted:',sorted(list1)) # [1, 2, 3, 4]
print('orginianllist',list1) # [2, 1, 4, 3]


#sort the list according to length of the string
items=['a','abcd','abced','abcde','abc']
def my_func(item):
  return len(item)
items.sort(key=my_func)
print(items) # ['a', 'abc', 'abcd', 'abced', 'abcde']

#sort the list according to length of the string in desc order . Note strings of equal lenth are placed in any order
items=['a','abcd','abcde','abced','abc','x']
items.sort(reverse=True,key=my_func)
print(items) # ['abcde', 'abced', 'abcd', 'abc', 'a', 'x']
items=['x','abcd','abcde','abced','abc','a']
items.sort(reverse=False,key=my_func)
print(items) # ['x', 'a', 'abc', 'abcd', 'abcde', 'abced']

#reverse the list
items=['a','b','c','d','g','x','k','v']
items.reverse()
print('reverse list:',items) # ['v', 'k', 'x', 'g', 'd', 'c', 'b', 'a']

#count the item in ths list
items=['a','v','c','v','g','x','k','v']
x=items.count('v')
print('count:',x) # 3
x=items.count('ko')
print('count:',x) # 0

#length
items=['a','v','c','v','g','x','k','v']
x=len(items)
print(x) #8

# copy - shallow copy
items1=['a','v','c','v','g','x','k','v']
items2=items1
items1.pop()
print(items1) #['a', 'v', 'c', 'v', 'g', 'x', 'k']
print(items2) #['a', 'v', 'c', 'v', 'g', 'x', 'k']

# merge two lists
list1=[1,2,3]
list2=[7,8,9]
list=list1+list2
print(list)

#max value
list1=[2,3,1000]
print(max(list1)) # 1000
names = ['Adams', 'Ma', 'diMeola', 'Zandusky']
print(max(names)) #'diMeola'


#min value
list1=[2,3,1000]
print(min(list1)) # 2

# key function used with sort
names = ['Adams', 'Ma', 'diMeola', 'Zandusky']
def lowercaseof(anystring):
  return anystring.lower()
names = ['Adams', 'Ma', 'diMeola', 'Zandusky']
print(names.sort(key=lowercaseof)) # 'Adams', 'diMeola', 'Ma', 'Zandusky'

# lambda key function used with sort
names = ['Adams', 'Ma', 'diMeola', 'Zandusky']
names.sort(key=lambda anystring:anystring.lower()) # ['Adams', 'diMeola', 'Ma', 'Zandusky']
print(names)

# lambda key function used with max
names = ['Adams', 'Ma', 'diMeola', 'Zandusky']
print(max(names,key=lambda anystring:len(anystring))) #'Zandusky'

# lambda key function used with max
data = [[12587961, 0.7777777777777778], [12587970, 0.5172413793103449], [12587979, 0.3968253968253968], [12588042, 0.9473684210]]
print(max(data,key=lambda item:item[1])) #[12588042, 0.947368421]
index, value=max(data,key=lambda item:item[1])
print(index,value) # 12588042 0.947368421

# list explode
list1=[1,2]
x,y=list1
print(x,y) # 1 2
#x,y,z=list1 # error not enough values to unpack


#max, all values must be of same type
list1=[1,2,'x']
#max(list1) # TypeError
list1=['1','2','x']
max(list1) # 'x'

