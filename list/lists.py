items=[2,3,4,5,6,7,8,9,10]
items2=items

print(hex(id(items)), hex(id(items2)))

#insert at 0th position
items.insert(0,1)

#list comprehension
# Given a list of strings,  the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
def match_ends(words):
  # +++your code here+++
  alist=[x for x in words if len(x) >1 and x[0] == x[-1]]
  return len(alist)


# add an item, use append and not index
items=[]
items.append(11)
# items[1]=2 # renders error

# pop removes the last item and returns it
items=[1,2,3,6,8]
x=items.pop()
x
items

# update
# items[10]=11 >> error out of range
items[1]=2


#delete an item given index
del items[1]

#dleete a range
alist=[1,2,3,4,5]
del alist[-2:]   ## Delete last two elements
alist

#delete an item given value : first occurance only
items=['a','v','c','v','g','v','k','v']
items.remove('v')
print('remove:', items) #['a', 'c', 'v', 'g', 'v', 'k', 'v']


#search for all occurances , raises ValueError if item is not found
# x=items.index('v',x+1)>>  ValueError
items=['a','v','c','v','g','v','k','v']
indexes=[]
x=items.index('v')
while x >0:
  indexes.append(x)
  try:
    x=items.index('v',x+1)
  except Exception as e:
    print(e)
    break
indexes
# alternatively
indexes = [i for i, x in enumerate(items) if x == "v"]
indexes

# search if a value exists in a list
if 'v' in items:
  'yes'



#sort the list in asc oreder
items=['a','v','c','v','g','v','k','v']
items.sort()
print(items) #['a', 'c', 'g', 'k', 'v', 'v', 'v', 'v']

#sort the list in desc oreder
items=['a','b','c','d','g','x','k','v']
items.sort(reverse=True)
print('sort in reverse:',items) # ['x', 'v', 'k', 'g', 'd', 'c', 'b', 'a']

#sort vs sorted
list1=['a','b','c','ae']
x=sorted(list1)
x
list1

x=sorted(list1,reverse=True)
x
x=sorted(list1,reverse=True,key=lambda item:len(item))
x
x=sorted(list1,reverse=False,key=lambda item:len(item))
x


print('sorted:',sorted(list1)) # [1, 2, 3, 4]
print('orginianllist',list1) # [2, 1, 4, 3]


#sort the list according to length of the string

items=['a','abcd','abced','abcde','abc']
#items.sort(key=len)
items.sort(key=lambda item:len(item))
print(items) # ['a', 'abc', 'abcd', 'abced', 'abcde']



#sort the list according to length of the string in desc order . Note strings of equal lenth are placed in any order
items=['a','abcd','abcde','abced','abc','x']
items.sort(reverse=True,key=lambda item:len(item))
print(items) # ['abcde', 'abced', 'abcd', 'abc', 'a', 'x']
items=['x','abcd','abcde','abced','abc','a']
items.sort(reverse=False,key=lambda item:len(item))
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

#deep copy
print('deep copy)')
alist=[1,2,3,4,5]
blist=alist
clist=[]
clist[:]=alist[:]
alist.pop()
print(alist) #[1, 2, 3, 4]
print(blist) #[1, 2, 3, 4]
print(clist) #[1, 2, 3, 4, 5]




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


# lambda key function used with sort
names = ['Adams', 'Ma', 'diMeola', 'Zandusky']
names.sort(key=lambda item:item.lower()) # ['Adams', 'diMeola', 'Ma', 'Zandusky']
names

# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
alist=[(1, 7), (1, 3), (3, 2, 5), (2, 2)]
alist.sort(key=lambda atuple: atuple[-1])
print('sorted tuple list', alist) # [(2, 2), (1, 3), (3, 4, 5), (1, 7)]



# lambda key function used with max
names = ['Adams', 'Ma', 'DiMeolaswqxqwdqwc', 'Zandusky']
max(names) ##'Zandusky'
print(max(names,key=lambda anystring:len(anystring))) # DiMeolaswqxqwdqwc

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

# get slice
alist=[1,2,3,4,5,6]
blist=alist[2:4]
print(blist) # [3, 4]


# set slice
alist=[1,2,3,4,5,6]
blist=[10,11,12]
alist[:2] =blist[:2]
print(alist) #[10, 11, 3, 4, 5, 6]

# insert a list into another at given index:
alist=[1,2,3,4,5,6]
print(alist[2:2]) #[]
blist=[10,11,12]
alist[2:2] =blist[:]
print(alist) # [1, 2, 10, 11, 12, 3, 4, 5, 6]

alist=[1,2,3,4,5,6]
print(alist[2:3]) #[3]
blist=[10,11,12]
alist[2:3] =blist[:]
print(alist) # [1, 2, 10, 11, 12, 4, 5, 6]


