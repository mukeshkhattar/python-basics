'''
Implementtaion of a stack using List class
the end of the list will hold the top element of the stack.
 This is more efficient than alternative where the first element of list holds top

'''

class Stack:
  def __init__(self):
    self.items=[]

  def isEmpty(self):
    return self.items == []

  def pop(self):
    if self.isEmpty():
      return float('-inf')
    else:
      return self.items.pop()

  def push(self,item):
    self.items.append(item)

  def peek(self):
    if self.isEmpty():
      return float('-inf')
    else:
      return self.items[len(self.items)-1]

  def size(self):
    return len(self.items)



