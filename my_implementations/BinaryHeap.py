class BinaryHeap:
	def __init__(self):
		self.heap = [0]
		self.size = 0

	def __swim(self, key):
		while key // 2 > 0:
			parentKey = key // 2
			if self.heap[key] > self.heap[parentKey]:
				temp = self.heap[parentKey]
				self.heap[parentKey] = self.heap[key]
				self.heap[key] = temp
			key = key // 2

	def insert(self, value):
		self.heap.append(value)
		self.size += 1
		self.__swim(self.size)

	def sink(self, key):
		while key * 2 < self.size:
			child = key * 2
			if child < self.size and self.heap[child] < self.heap[child+1]:
				child += 1 # right child is larger
			if child < key:
				break
			temp = self.heap[child]
			self.heap[child] = self.heap[key]
			self.heap[key] = temp
			key = child

	def deleteMax(self):
		maxItem = self.heap[1]
		self.heap[1] = self.heap.pop()
		self.sink(1)
		self.size -= 1
		return maxItem

	def isValid(self):
		isValid = True
		for i in range(1,self.size):
			childKey = i * 2
			if childKey < self.size and self.heap[childKey] > self.heap[i]:
					isValid = False
			if childKey + 1 < self.size and self.heap[childKey + 1] > self.heap[i]:
					isValid = False	
		return isValid		

	def show(self):
		for key in self.heap:
			print(key, end=' ')
		print()

bheap = BinaryHeap()
bheap.insert(2)
bheap.insert(5)
bheap.insert(11)
bheap.insert(7)
bheap.insert(66)
bheap.insert(30)
bheap.insert(21)
bheap.insert(19)
bheap.insert(44)
bheap.show()
assert bheap.isValid()

bheap.heap[1] = 10
bheap.sink(1)
bheap.show()
assert bheap.isValid()

print("max", bheap.deleteMax())
assert bheap.isValid()