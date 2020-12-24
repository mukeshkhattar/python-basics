class Node:
  # Function to initialize the node object
  def __init__(self, data):
    self.data = data  # Assign data
    self.next = None  # Initialize

# driver code
if __name__ == '__main__':
  first=Node(1)
  type(first)
  first.data
  if first.next == None:
    'None'
  id(first)
  id(Node(1))
  id(Node(1))
  id(Node(1))

