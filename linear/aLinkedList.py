# A simple Python program to introduce a linked list

class Node:
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null


# Linked List class contains a Node object
class LinkedList:
	def __init__(self):
		self.head = None


# Code execution starts here
if __name__=='__main__':

	# Start with the empty list
	llist = LinkedList()

	llist.head = Node(1)
	second = Node(2)
	third = Node(3)
	llist.head.next = second; # Link first node with second
	second.next = third; # Link second node with the third node

print(llist.head.data)
llist.head.next.next.data
if llist.head.next.next.next == None:
  'end'



