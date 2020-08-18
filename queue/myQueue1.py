'''
Implementtaion of a queue using List class
the end of the list = rear of the queue
the begining of the list = front of the queue
enqueue = O(1)
dequeue = O(n)
'''

class Queue:
  def __init__(self):
    self.items=[]

  def isEmpty(self):
    return self.items == []

  def dequeue(self):
    if self.isEmpty():
      return float('-inf')
    else:
      return self.items.pop(0)

  def enqueue(self,item):
    self.items.append(item)


  def size(self):
    return len(self.items)

  def __repr__(self):
    return str(self.items)


if __name__ == '__main__':
  s=Queue()
  s.enqueue(10)
  s.enqueue(11)
  s.dequeue()
  print(s) # 11

