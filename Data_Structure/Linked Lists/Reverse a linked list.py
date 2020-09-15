#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the reverse function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reverse(head):
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_singly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()

----------------------------------------------------------------------------
						# Solution
						
def reverse_iterative(head):
	# e.g. A > B > C > D
	if head:
		current_node = head  # current = A
		next_node = current_node.next  # next = A.next = B
		current_node.next = None  # A > None
		while next_node:
			tmp = next_node.next  # tmp = B.next = C
			next_node.next = current_node  # B.next = current = A
			head = current_node = next_node  # head = current = B
			next_node = tmp  # next = tmp = C
	return head


def reverse_stack(head):
	# e.g. A > B > C > D
	if head:
		stack = [head]
		while stack[-1].next:
			node = stack[-1]
			stack.append(node.next)
		# stack = [D, C, B, A]
		head = stack.pop()  # head = D
		current = head  # current = head = D
		while stack:
			node = stack.pop()  #
			current.next = node
			current = current.next
		current.next = None
	return head


def reverse_recursive(head):
	if not head:
		return head
	else:
		head = reverse_recursive(head.next)
	return head
