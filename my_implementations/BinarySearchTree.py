import queue

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.count = 1

class BST:
  def __init__(self):
    self.root = None

  def computeSize(self, node, count = 0):
    if node:
      count = 1
      if node.left:
        count += self.size(node.left, count)
      if node.right:
        count += self.size(node.right, count)
    return count

  def getCount(self, node):
    if node:
      return node.count
    return 0

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
    else:
      node.value = value
    node.count =  1 + self.getCount(node.left) + self.getCount(node.right)
    return node

  # aka LNR
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

      print(f'node:{currentNode.value} level:{currentLevel} count:{currentNode.count}')

      level = currentLevel + 1
      if currentNode.left:
        nodeQueue.put((currentNode.left, level))
      if currentNode.right:
        nodeQueue.put((currentNode.right, level))

  def delete(self, value):
    self.__delete(self.root, value)

  def __delete(self, node, value):
    if node == None:
      return
    if value < node.value:
      node.left = self.__delete(node.left, value)
    elif value > node.value:
      node.right = self.__delete(node.right, value)
    else:
      if not node.left:
        temp = node.right
        node = None
        return temp
      if not node.right:
        temp = node.left
        node = None
        return temp
      ceiling = self.__min(node.right)
      node.value = ceiling.value
      node.right = self.__delete(node.right, ceiling.value)
    return node

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

  # good for visiting leaves first (travel all the way down left tree then right)
  # also good for deleting/ freeing the tree without losing refs
  # LRN 
  def postOrder(self):
    print("post order traversal")
    self.__postOrder(self.root)

  def __postOrder(self, node):
    if node == None:
      return
    if node.left:
      self.__postOrder(node.left)
    if node.right:
      self.__postOrder(node.right)

  # good for visiting top nodes first (travel all the way down left tree then right)
  # also used for copying trees
  # NLR
  def preOrder(self):
    print("pre order traversal")
    self.__preOrder(self.root)

  def __preOrder(self, node):
    if node == None:
      return
    print(node.value)
    if node.left:
      self.__preOrder(node.left)
    if node.right:
      self.__preOrder(node.right)

  def getLeaves(self):
    print("get leaves")
    self.__getLeaves(self.root)

  def __getLeaves(self, node):
    if node == None:
      return
    if not node.left and not node.right:
      print(node.value)
    if node.left:
      self.__getLeaves(node.left)
    if node.right:
      self.__getLeaves(node.right)

tree = BST()
tree.insert(11)
tree.insert(2)
tree.insert(6)
tree.insert(55)
tree.insert(12)
tree.insert(4)
tree.insert(33)
tree.insert(7)
tree.inOrderTraversal() 
tree.bfs()
# pre/ post/ in order are types of DFS
tree.postOrder()
tree.preOrder()

tree.getLeaves()

assert tree.min().value == 2
assert tree.max().value == 55

assert tree.floor(12).value == 12
assert tree.floor(60).value == 55
assert tree.floor(8).value == 7
assert tree.floor(3).value == 2

assert tree.ceiling(10).value == 11
assert tree.ceiling(50).value == 55
assert tree.ceiling(30).value == 33
assert tree.ceiling(1).value == 2

print("---delete 55")
tree.delete(11)
tree.bfs()

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
