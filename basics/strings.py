

'''
count(item)
endswith(string1)
find(item) - returns index of first occurrence of item
split(schar) returns list
'''

# count
item='sxcbxcixc'
item.count('xc') # 3

# endswith
'sxcewcec'.endswith('cec') # True
'sxcewcec'.endswith('d') # False

#startswith

#find, returns index of first occurance if found, otherwise -1
'sxcewcec'.find('xc') # 1
'sxcewcec'.find('xcwdwd') # -1

#index, returns index of first occurance if found, otherwise ValueEroor
'sxcewcec'.index('xc') # 1
'sxcewcec'.find('xcwdwd') # ValueErro

# rfind(sub[, start[, end]]
'12ece12'.rfind('12') #5
'12ece12'.rfind('120') #-1
# rindex - like rfind, but raises ValueEroor when not found



#split - returns list
'x1x23x456x789x'.split('x') # ['', '1', '23', '456', '789', '']


'''
isalpha(),
isnumeric()
isalphanum()
'''

#replace
'qw123'.replace('123','45') # 'qw45'
'qw123'.replace('1234','45') # 'qw123'

#strip
'   spacious   '.strip() #'spacious'
'www.example.com'.strip('cmowz.') # 'example'


#sort vs sorted
x='caebd1'
x_sorted_list=sorted(x)
x_sorted_string=''.join(x_sorted_list)
print('sorted:',x_sorted_string) # 1abcde


#reverse the string
x='caebd1'
list1=[] # this is needed before the assignment in next line, otherwise nameError
list1[:]=x
list1.reverse()
x_reversed_string=''.join(list1)
print('reversed string:',x_reversed_string)


#length
x='caebd1'
l=len(x)
print('len:',len(x)) #6

# copy - shallow copy
x='caebd1'
y=x
print(id(x)) #4373360304
print(id(y)) #4373360304

# merge two lists
x='caebd1'
y='234'
z=x+y
print(z) # caebd1234
