items=[2,3,4,5,6,7,8,9,10]
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
#delete
del items[1]
print(items) # 1,3,4,...10
items.insert(1,2)
print(items) # 1,2,3,4,...10
#search
x=items.index(5)
print(x, type(x)) # prints 4, int
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
#sort
#sort the list in asc oreder
items.sort()
print(items) #['a', 'c', 'g', 'k', 'v', 'v', 'v', 'v']
#sort the list in desc oreder
items=['a','b','c','d','g','x','k','v']
items.sort(reverse=True)
print('sort in reverse:',items) # ['x', 'v', 'k', 'g', 'd', 'c', 'b', 'a']
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
