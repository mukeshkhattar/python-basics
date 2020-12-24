''' This program checks if symbols given in string are balanced or not
e.g. '(7*[8*[6+7]])' is balanced
'''
from myStack import Stack
def isStringBalanced(inputString):
  opening_list=['[','(','{']
  closing_list=[']',')','}']
  currentStack=Stack()
  for char in inputString:
    if char in opening_list:
      currentStack.push(char)
    elif char in closing_list:
      char1=currentStack.pop()
      if char1 in opening_list and (opening_list.index(char1) == closing_list.index(char)):
        continue
      else:
        return False
    else:
      continue
  if currentStack.isEmpty():
    return True
  else:
    return False

if __name__ == '__main__':
  test_string= ')[1+2]('
  print(isStringBalanced(test_string))


