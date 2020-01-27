class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.count = 0
  
  def prepend(self, value):
    oldHead = self.head
    self.head = Node(value)
    self.head.next = oldHead
    self.count += 1

  def length(self):
    return self.count

  def get(self, index):
    if index < 0 or index > self.count:
      return None
    
    current = self.head
    for _ in range(index):
      current = current.next

    return current.value

  def append(self, value):
    current = self.head
    if not self.head:
      self.head = Node(value)
      self.count += 1
      return
    
    while current.next:
      current = current.next
    
    current.next = Node(value)
    self.count += 1

  def remove(self, value):
    if not self.head:
      return

    if self.head.value == value:
      self.head = self.head.next
      self.count -= 1
      return

    prev = self.head
    current = self.head.next

    while current:
      if current.value == value:
        prev.next = current.next
        self.count -= 1
        break
      prev = prev.next
      current = current.next

  def insert(self, value, index):
    if index < 0 or index > self.count:
      return

    if index == 0:
      self.prepend(value)
      return
    
    current = self.head
    for _ in range(index - 1):
      current = current.next

    oldNext = current.next 
    current.next = Node(value)
    current.next.next = oldNext
    self.count += 1

  def show(self):
    current = self.head
    while current:
      print(current.value,)
      current = current.next

linkedList = LinkedList()
linkedList.prepend("a")
linkedList.prepend("b")
linkedList.prepend("c")
linkedList.prepend("d")

assert linkedList.get(0) == "d"
assert linkedList.get(1) == "c"
assert linkedList.get(2) == "b"
assert linkedList.get(3) == "a"
assert linkedList.length() == 4

assert linkedList.get(-1) == None
assert linkedList.get(5) == None

linkedList.append("1")
linkedList.append("2")
linkedList.append("3")

assert linkedList.get(0) == "d"
assert linkedList.get(1) == "c"
assert linkedList.get(2) == "b"
assert linkedList.get(3) == "a"
assert linkedList.get(4) == "1"
assert linkedList.get(5) == "2"
assert linkedList.get(6) == "3"
assert linkedList.length() == 7

linkedList.remove("1")
linkedList.remove("b")
linkedList.remove("d")
linkedList.remove("d")

assert linkedList.get(0) == "c"
assert linkedList.get(1) == "a"
assert linkedList.get(2) == "2"
assert linkedList.get(3) == "3"
assert linkedList.length() == 4

emptyList = LinkedList()

emptyList.remove("abc")
assert emptyList.length() == 0
assert emptyList.head == None

emptyList.append("def")
assert emptyList.head.value == "def"
assert emptyList.length() == 1

emptyList.remove("abc")
assert emptyList.head.value == "def"
assert emptyList.length() == 1
  
emptyList.remove("def")
assert emptyList.head == None
assert emptyList.length() == 0

linkedList2 = LinkedList()
linkedList2.append(1)
linkedList2.append(2)
linkedList2.append(5)
linkedList2.append(8)
linkedList2.insert(3, 0)
linkedList2.insert(6, 2)
linkedList2.insert(22, -1)
linkedList2.insert(22, 10)
linkedList2.insert(19, 6)

assert linkedList2.get(0) == 3
assert linkedList2.get(2) == 6
assert linkedList2.get(6) == 19
assert linkedList2.length() == 7
