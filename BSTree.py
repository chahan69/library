from random import random

class Node(object):
	def __init__(self, key, x=None):
		if x == None:
			self.data = key
		else:
			self.data = x
		self.key   = key
		self.priority = random()
		self.left  = None
		self.right = None

# 右回転
def rotate_right(node):
    lnode = node.left
    node.left = lnode.right
    lnode.right = node
    return lnode

# 左回転
def rotate_left(node):
    rnode = node.right
    node.right = rnode.left
    rnode.left = node
    return rnode

def wrapped_put(node, key, x=None):
	if node is None:
		return(Node(key,x))
	elif key==node.key:
		node.data = x
		return(node)
	elif key<node.key:
		node.left = wrapped_put(node.left,key,x)
		if node.priority < node.left.priority:
			node = rotate_right(node)

	else:
		node.right = wrapped_put(node.right,key,x)
		if node.priority < node.right.priority:
			node = rotate_left(node)
	return(node)


def wrapped_delete(node, key):
	def search_min(node):
		if node.left is None: return node.data
		return search_min(node.left)

	def delete_min(node):
		if node.left is None: return node.right
		node.left = delete_min(node.left)
		return node

	if node is not None:
		if key == node.key:
			if node.left is None and node.right is None:
				return None
			elif node.left is None:
				node = rotate_left(node)
			elif node.right is None:
				node = rotate_right(node)
			else:
				if node.left.priority < node.right.priority:
					node = rotate_right(node)
				else:
					node = rotate_left(node)
			node = wrapped_delete(node, key)
		elif key < node.key:
			node.left = wrapped_delete(node.left, key)
		else:
			node.right = wrapped_delete(node.right, key)
	return node

class BSTree(Node):
	def __init__(self):
		import sys
		sys.setrecursionlimit(10**6)
		self.root = None

	def get(self, key):
		node = self.root
		while node:
			if node.key == key:
				return node.data
			if key < node.key:
				node = node.left
			else:
				node = node.right
		return False

	def put(self, key, x=None):
		self.root=wrapped_put(self.root, key, x)

	def delete(self, key):
		self.root=wrapped_delete(self.root,key)

	def traverse(self):
		def wrapped_traverse(node):
			if node:
				for x in wrapped_traverse(node.left):
					yield x
				yield (node.key, node.data)
				for x in wrapped_traverse(node.right):
					yield x
		return(wrapped_traverse(self.root))

if __name__ == '__main__':
	t=BSTree()

	from random import randint
	for j in [randint(10,100) for i in range(100)]:
		t.put(j,45)

	print([i for i in t.traverse()])

	print(t.get(51))
	t.put(51, "UHO")
	print(t.get(51))
	t.delete(51)
	print(t.get(51))















