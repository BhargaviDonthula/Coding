class Heap():
	def __init__(self):
		self.li = [1, 2,3,4,5,6,7,8,9]
		self.size = len(self.li)

	def heappush(self, element):
		self.li.append(element) 
		curr = self.size
		self.size += 1
		while curr > 0 and self.li[curr] > self.li[(curr - 1) // 2]:
			self.li[curr], self.li[(curr - 1)// 2] = self.li[(curr - 1) // 2], self.li[curr]
			curr = (curr - 1)// 2  
		print(self.li)

		
	def get_left_child(self, child):
		left = 2 * child + 1
		return left if left < self.size else None 

	def get_right_child(self, child):
		right = 2 * child + 2
		return right if right < self.size else None 

	def get_parent(self, i):
		return i // 2 if i > 0 else None

	def maxheapify(self, i):
		curr = i
		left = self.get_left_child(i)
		right = self.get_right_child(i)
		if left and self.li[left] > self.li[i]:
			i = left
		if right and self.li[right] > self.li[i]:
			i = right	

		if curr != i:
			self.li[curr], self.li[i] = self.li[i], self.li[curr]
			self.maxheapify(i)


	def build_heap(self):
		print(self.li)		
		for i in range(self.size // 2, -1, -1):
			self.maxheapify(i)
		print("List after Heapify:")
		print(self.li)
		

	def heappop(self):
		self.size -= 1
		self.li[0], self.li[self.size] =  self.li[self.size], self.li[0]
		val = self.li.pop()
		self.maxheapify(0)
		print(self.li)
		return val

heap = Heap()
print("List before Heapify:")
heap.build_heap()
print("List after inserting 10:")
heap.heappush(10)
print("List after popping max:")
val = heap.heappop()
print("Removed max element:", val)
