# sort the dict by descending order of values
adict= {}
adict['a']=1
adict['b']=10
adict['z']=2
adict['x']=5
adict['y']=7

alist_items=adict.items()
# alist_items is a list and hence can be sorted:
sorted_list_items=sorted(alist_items, key=lambda item:item[1], reverse=True)
for k,v in sorted_list_items:
  print(k,v)
'''
output
b 10
y 7
x 5
z 2
a 1
'''

