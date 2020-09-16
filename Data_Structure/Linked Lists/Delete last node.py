from . import Node

def delete-last_node(head):
	if head:
		previous = None
		temp = head
		while temp.next is not None:
			previous = temp
			temp = temp.next
		previous.next = None
		return head
	else:
		print('List doesn't exists')
