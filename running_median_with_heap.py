class Heap():
	def __init__(self):
		self.elements = []

	def get_size(self):
		return len(self.elements)

	def insert(self, num):
		self.elements.append(num)
		self.heapify_up()

	def heapify_up(self):
		i = len(self.elements) - 1
		while i//2 >= 0 and self.compare(self.elements[i//2], self.elements[i]):
			self.elements[i], self.elements[i//2] = self.elements[i//2], self.elements[i]
			i = i//2

	def get_top(self):
		return self.elements[0]

	def remove_top(self):
		n = self.get_size()
		if  n > 0:
			self.elements[0], self.elements[n-1] = self.elements[n-1], self.elements[0]
			top_child = self.elements.pop()
			self.heapify_down()
			return top_child

	def heapify_down(self):
		i = 0
		while i*2 < self.get_size():
			ch_ind = self.select_child(i)
			if self.compare(self.elements[i], self.elements[ch_ind]):
				self.elements[i], self.elements[ch_ind] = self.elements[ch_ind], self.elements[i]
				i = ch_ind
			else:
				break

	def select_child(self, i):
		ch_ind = i*2
		if i*2+1 < self.get_size() and self.compare(self.elements[ch_ind], self.elements[i*2+1]):
			ch_ind = i*2+1
		return ch_ind


class MinHeap(Heap):
	def __init__(self):
		super().__init__()

	def compare(self, a, b):
		return a > b


class MaxHeap(Heap):
	def __init__(self):
		super().__init__()

	def compare(self, a, b):
		return a < b

#-----------------------------------------------------------------

def comp(n, m):
	return (n>m) - (n<m)

def get_median(num, median, left_heap, right_heap):
	left_size = left_heap.get_size()
	right_size = right_heap.get_size()

	if left_size > right_size: 
		if num < median: # fits to left heap
			left_top = left_heap.remove_top()
			right_heap.insert(left_top)
			left_heap.insert(num)
		else:  # fits to right heap
			right_heap.insert(num)
		return (left_heap.get_top() + right_heap.get_top())/2
	elif left_size < right_size:
		if num < median: # fits to left heap
			left_heap.insert(num)
		else:  # fits to right heap
			right_top = right_heap.remove_top()
			left_heap.insert(right_top)
			right_heap.insert(num)
		return (left_heap.get_top() + right_heap.get_top())/2
	else:
		if num < median: # fits to left heap
			left_heap.insert(num)
			return left_heap.get_top()
		else:  # fits to right heap
			right_heap.insert(num)
			return right_heap.get_top()


if __name__ == '__main__':

	left_heap = MaxHeap()  # max heap
	right_heap = MinHeap() # min heap

	median_list = []

	n = int(input())
	median = 0
	for i in range(n):
		num = int(input())
		median = get_median(num, median, left_heap, right_heap)
		median_list.append(round(float(median),1))

	for m in median_list:
		print(m)
