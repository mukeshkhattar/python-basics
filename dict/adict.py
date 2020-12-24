from collections import Counter
import re
'''
# Dictionary - key value pairs
Strategy note - from a performance point of view, the dictionary is a greatest tool.
It is much faster than lists in operations like contains, get_item,set_item etc.
It implements hashTable or HashMap in Pythin
#  you should use it where you can as an easy way to organize data.
1. For example, you might read a log file where each line begins with an IP address,
2. store the data into a dict using the IP address as the key, and the list of lines  as the value.
3. Once you've read in the whole file, you can look up any IP address and instantly see its list of lines.
4. The dictionary takes in scattered data and makes it into something coherent.
'''
# add
# update
adict={}
adict['b']=10
adict['z']=2
adict['x']=5
adict['y']=7
adict['b']=11
adict

#get value for a given key

adict['z']
'b' in adict  # returns True if key is dict
adict.get('tt') # returns value, otherwise None
adict.get('tt','alt') # returns value, otherwise alt;

#delete entry
del adict['b'] # deletes the entry
del adict['b'] # KeyErrror

#no duplicates of key - If a key is specified multiple times, only the latest value is used.
adict['b']=11
adict['b']=12
adict['b'] # 12

#get all keys
adict.keys() # returns all keys in dict_keys object.
#You cannot add or remove elements from a dict_keys object.

#iterate: the keys are in a random order.
for key in adict: print(key)

# get all values in dict_values([2, 5, 7, 11])
adict.values()

#get all key value paris
adict.items() # returns all key-value pairs in dict_items object. Each entry is a tuple(key,value)
for k, v in adict.items(): print (k, '>', v)

#key presence : use either :
'b' in adict # True
'b' in adict.keys() # True


#find if a value exists in dict
#there is no method to find if a value exists in dictionary


#a list can be implemented using dictionary e.g. like this -
adict1={j:None for j in range(100)}
adict1

# sort the dict by descending order of values
#sort - convert dict to list of tuples and then sort
alist_items=adict.items()
# alist_items is a list (of tuples) and hence can be sorted:
sorted_list_items=sorted(alist_items, key=lambda item:item[1], reverse=True)
for k,v in sorted_list_items:
  print(k,v)

id(sorted_list_items)
id(alist_items)
sorted_list_items
alist_items
type(alist_items)
type(sorted_list_items)
'''
output
b 11
y 7
x 5
z 2
a 1
'''

# counter example-1
alist=[1,2,3,4,4,3]
mydict=Counter(alist)
mydict #Counter({3: 2, 4: 2, 1: 1, 2: 1})

# counter example-2
aset={1,2,3,4,4,3}
mydict=Counter(aset)
mydict #Counter({1: 1, 2: 1, 3: 1, 4: 1})

# most common using counter
astring='2w2ew2e'
mydict=Counter(astring)
mydict=mydict.most_common(2)
for k,v in mydict:
  k + ':' + str(v)
'''
'2:3'
'w:2'
'''

# % operator works conveniently to substitute values from a dict into a string by name:
adict2 = {}
adict2['word'] = 'garfield'
adict2['count'] = 42
s = 'I want %(count)d copies of %(word)s' % adict2
s


