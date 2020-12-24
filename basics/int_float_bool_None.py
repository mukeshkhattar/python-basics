'''
int
float
bool
None - It has one only value : None
'''
# -inf
a=float('-inf')
type(a)
a
if a == float('-inf'):
  'yes'

# int operator gives floor value in int, do not use round :
round(2.5) #2
round(1.5) # 2
int(1.5) # 1
int(2.5) # 2

#None
a=None
type(a) # <class 'NoneType'>
if a == None:
  'yes'
  a # does not print anything

