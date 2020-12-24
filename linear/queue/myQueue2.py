'''
Implementtaion of a queue using collections.deque class

enqueue = O(1)
dequeue = O(n)
'''
from collections import deque
class Queue:
  def __init__(self):
    self.items=deque()

  def isEmpty(self):
    if self.items:
      return False
    else:
      return True

  def dequeue(self):
    if self.isEmpty():
      return float('-inf')
    else:
      return self.items.popleft()

  def enqueue(self,item):
    self.items.append(item)


  def size(self):
    return len(self.items)

  def __repr__(self):
    return str(list(self.items))


if __name__ == '__main__':
  s=Queue()
  s.enqueue(10)
  s.enqueue(11)
  s.dequeue()
  print(s) # 11

