import queue

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
    if value < node.value:
      if node.left is None:
        node.left = Node(value)
      else:
        self.__insert(node.left, value)
    elif value > node.value: 
      if node.right is None:
        node.right = Node(value)
      else:
        self.__insert(node.right, value)

  def inOrderTraversal(self):
    print("traverse tree in order (smallest to largest node)")
    self.__inOrderTraversal(self.root)

  def __inOrderTraversal(self, node):
    if node.left:
      self.__inOrderTraversal(node.left)
    print(node.value)
    if node.right:
      self.__inOrderTraversal(node.right)

  def bfs(self):
    print("bfs: traverse tree level by level")
    level = 0
    nodeQueue = queue.Queue()
    nodeQueue.put((self.root, level))
    while not nodeQueue.empty():
      current = nodeQueue.get()
      currentNode = current[0]
      currentLevel = current[1]

      print(f'node:{currentNode.value} level:{currentLevel}')

      level = currentLevel + 1
      if currentNode.left:
        nodeQueue.put((currentNode.left, level))
      if currentNode.right:
        nodeQueue.put((currentNode.right, level))

  def min(self):
    if self.root == None:
      return None
    return self.__min(self.root)

  def __min(self, node):
    if node.left == None:
      return node
    return self.__min(node.left)

  def max(self):
    if self.root == None:
      return None
    return self.__max(self.root)

  def __max(self, node):
    if node.right == None:
      return node
    return self.__max(node.right)

  # find the largest value smaller than arg
  def floor(self, value):
    return self.__floor(self.root, value)

  def __floor(self, node, value):
    if node == None:
      return None # case 0: either root null or reached end
    if value == node.value: # case 1: current node matches
      return node
    if value < node.value: # case 2: current node too big, go smaller
      return self.__floor(node.left, value)
    
    # case 3: current node too small, go bigger
    # value > node.value so we have to look for smallest on the right subtree
    # if we cannot find smaller than current node on right subtree then return current node
    rightSubTreeFloor = self.__floor(node.right, value)
    if rightSubTreeFloor == None:
      return node
    return rightSubTreeFloor

  def ceiling(self, value):
    return self.__ceiling(self.root, value)

  def __ceiling(self, node, value):
    if node == None:
      return None
    if value == node.value:
      return node
    if value > node.value: # current node too small, go bigger
      return self.__ceiling(node.right, value)
    
    # current node is larger, look for smallest on left subtree
    leftSubtreeCeiling = self.__ceiling(node.left, value)
    if leftSubtreeCeiling == None:
      return node
    return leftSubtreeCeiling

tree = BST()
tree.insert(11)
tree.insert(2)
tree.insert(6)
tree.insert(55)
tree.insert(12)
tree.inOrderTraversal() 
tree.bfs()

assert tree.min().value == 2
assert tree.max().value == 55

assert tree.floor(12).value == 12
assert tree.floor(60).value == 55
assert tree.floor(8).value == 6
assert tree.floor(3).value == 2

assert tree.ceiling(10).value == 11
assert tree.ceiling(50).value == 55
assert tree.ceiling(30).value == 55
assert tree.ceiling(1).value == 2


#   11
# 2   55 
#  6 12

# stack frame trace of inOrderTraversal()
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
