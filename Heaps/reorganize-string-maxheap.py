from collections import Counter

class Heapq():
	def __init__(self, heap):
		self.size = len(heap)

	def get_parent(self, child):
		return (child - 1) // 2 if child else -1

	def get_left_child(self, parent):
		child =  2 * parent + 1
		return child if child < self.size else None

	def get_right_child(self, parent):
		child = 2 * parent + 2
		return child if child < self.size else None

	def heappush(self, heap, element):
		heap.append(element)
		curr = self.size
		self.size += 1
		parent = self.get_parent(curr)
		print("heap before heapify in push", heap)
		
	
		while(parent >= 0 and heap[parent] < heap[curr]):
			heap[parent], heap[curr] = heap[curr], heap[parent]
			curr = parent
			parent = self.get_parent(curr)
		print("heap after heapify in push:", heap)

	def heappop(self, heap):
		if not heap:
			return None
		self.size -= 1
		heap[0], heap[self.size] = heap[self.size], heap[0]
		popped = heap.pop()
		self.convert_to_heap(heap, 0)
		return popped

	def convert_to_heap(self, heap, i):
		curr = i
		if not heap:
			return heap
		left = self.get_left_child(i)
		right = self.get_right_child(i)
		if left and heap[left] > heap[i]:
			i = left
		if right and heap[right] > heap[i]:
			i = right
		if curr != i:
			heap[curr], heap[i] = heap[i], heap[curr]
			self.convert_to_heap(heap, i)

	def heapify(self, heap):
		for i in range(self.size // 2, -1, -1):
			self.convert_to_heap(heap, i)

	def __del__(self):
		pass


class Solution:
	def reorganizeString(self, S):
		heap = []
		res = []
		n = len(S)
		for k,v in Counter(S).items():
			if v > (n + 1) // 2:
				return ""
			heap.append((v, k))
		heapq = Heapq(heap)
		heapq.heapify(heap)
		print("heap after heapify:", heap)
		while(len(heap) >= 2):
			#print("heap before:", heap)
			cnt1, val1 = heapq.heappop(heap)
			cnt2, val2 = heapq.heappop(heap)
			#print("heap after:", heap)
			res.append(val1)
			res.append(val2)
			#print(res)
			if cnt1 - 1 > 0:
				heapq.heappush(heap, (cnt1 - 1, val1))
			if cnt2 - 1 > 0:
				heapq.heappush(heap, (cnt2 - 1, val2))
		if heap:
			res.append(heap[0][1])
		return "".join(res)


		


s = "bbbbayobq"
obj = Solution()
print(obj.reorganizeString(s))
