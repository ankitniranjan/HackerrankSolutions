from . import Node


def traverse_pre_order_recursive(root):
	if root:
		print(root.data, end=" ")
		traverse_pre_order_recursive(root.left, action)
		traverse_pre_order_recursive(root.right, action)


def traverse_pre_order_iterative(root):
	if root:
		stack = [root]
		while stack:
			node = stack.pop()
			print(node.data, end=" ")
			if node.right:
				stack.append(node.right)
			if node.left:
				stack.append(node.left)


root = Node("A")
root.left = Node("B")
root.left.left = Node("C")
root.left.right = Node("D")
root.right = Node("E")
root.right.left = Node("G")
root.right.right = Node("F")
