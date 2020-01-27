class HeapSort:
	def __init__(self):
		self.heap = [0]
		self.size = 0

	# append without heap ordering
	def append(self, value):
		self.heap.append(value)
		self.size += 1

	def sink(self, key):
		while key * 2 < self.size:
			child = key * 2
			if self.heap[key] > self.heap[child] and self.heap[key] > self.heap[child + 1]:
				break
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

	def convertToHeap(self):
		for i in range(len(self.heap) // 2, 0, -1):
			self.sink(i)
	
	def isValidHeap(self):
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

	def sort(self):
		for i in range(1, len(self.heap) - 1):
			top = self.deleteMax()
			print(i, top)
			assert self.isValidHeap()

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
hsort.sort()