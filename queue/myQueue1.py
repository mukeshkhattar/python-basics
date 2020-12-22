'''
Queue - FIFO
Implementtaion of a queue using python List class
the end of the list = rear of the queue
the begining of the list = front of the queue
enqueue = O(n)
dequeue = O(1)
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
      return self.items.pop()

  def enqueue(self,item):
    self.items.insert(0,item)


  def size(self):
    return len(self.items)


  def __repr__(self):
    print('called')
    return str(self.items)


if __name__ == '__main__':
  s=Queue()
  type(s)
  s.enqueue(10)
  s.enqueue(11)
  s.dequeue()
  print(s) # 11

