# this class creates max heap
class BinaryHeap:
	def __init__(self):
		self.heap = [0]
		self.size = 0

	def swim(self, key):
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
		self.swim(self.size)

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
		if self.size <= 0:
			return -1
		maxItem = self.heap[1]
		self.heap[1] = self.heap.pop()
		self.size -= 1
		self.sink(1)
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

# this class creates min heap
class HeapSort:
	def __init__(self):
		self.heap = [0]
		self.size = 0

	# append without heap ordering
	def append(self, value):
		self.heap.append(value)
		self.size += 1

	def convertToHeap(self):
		for i in range(len(self.heap) - 1, -1):
			# exchange last with root
			temp = self.heap[i]
			self.heap[i] = self.heap[1]
			self.heap[1] = temp
			# sink the new root into place
			self.sink(1)
	
	def isValidHeap(self):
		# check for min heap condition
		isValid = True
		for i in range(1,self.size):
			childKey = i * 2
			if childKey < self.size and self.heap[childKey] < self.heap[i]:
					isValid = False
			if childKey + 1 < self.size and self.heap[childKey + 1] < self.heap[i]:
					isValid = False	
		return isValid	

	def show(self):
		for key in self.heap:
			print(key, end=' ')
		print()

	def sort(self):
		# broken currently
		for i in range(len(self.heap) - 1):
			top = self.deleteMax()
			print(i, top)
			assert self.isValidHeap()
			# hsort.show()


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

hsort = HeapSort()
hsort.append(2)
hsort.append(5)
hsort.append(11)
hsort.append(7)
hsort.append(66)
hsort.append(30)
hsort.append(21)
hsort.append(19)
hsort.append(44)
hsort.convertToHeap()
hsort.show()
assert hsort.isValidHeap()
# hsort.sort()