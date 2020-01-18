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

	def show(self):
		for key in self.heap:
			print(key, end=' ')

bheap = BinaryHeap()
bheap.insert(2)
bheap.insert(5)
bheap.insert(11)
bheap.insert(7)
bheap.insert(66)
bheap.insert(30)
bheap.insert(21)
bheap.insert(19)
bheap.show()