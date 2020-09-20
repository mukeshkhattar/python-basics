from collections import Counter
import re
# sort the dict by descending order of values
adict={}
adict['b']=10
adict['z']=2
adict['x']=5
adict['y']=7

alist_items=adict.items()
# alist_items is a list (of tuples) and hence can be sorted:
sorted_list_items=sorted(alist_items, key=lambda item:item[1], reverse=True)
for k,v in sorted_list_items:
  print(k,v)

id(sorted_list_items)
id(alist_items)
sorted_list_items
alist_items
'''
output
b 10
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



