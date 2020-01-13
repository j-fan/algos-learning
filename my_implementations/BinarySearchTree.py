class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BST:
  def __init__(self):
    self.root = None

  def insert(self, value):
    if self.root == None:
      self.root = Node(value)
    else:
      self.__insert(self.root, value)

  def __insert(self, node, value):
    if node.value < value:
      if node.left is None:
        node.left = Node(value)
      else:
        self.__insert(node.left, value)
    elif node.value > value: 
      if node.right is None:
        node.right = Node(value)
      else:
        self.__insert(node.right, value)

  # traverse tree in order (largest to smallest node)
  def listTree(self):
    self.__listTree(self.root)

  def __listTree(self, node):
    if node.left:
      self.__listTree(node.left)
    print(node.value)
    if node.right:
      self.__listTree(node.right)

  # traverse tree level by level
  def bfs(self):
    print("unimplemented")

tree = BST()
tree.insert(11)
tree.insert(2)
tree.insert(6)
tree.insert(55)
tree.insert(12)
tree.listTree() #prints 55 12 11 6 2

#   11
# 2   55 
#  6 12

# stack frame trace of listTree()
# 11
# -> left -> 2
#            -> left -> null
#            -> print 2 -> right -> 6
#                                   -> left -> null
#                                   -> print 6 -> right -> null
#  -> print 11 -> right -> 55
#                           -> left -> 12
#                                       -> left -> null
#                                       -> print 12 -> right -> null
#                           -> print 55 -> right -> null
