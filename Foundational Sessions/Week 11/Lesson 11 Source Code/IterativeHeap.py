class IterativeHeap:
    def __init__(self):
        self.heap = []

    def insert(self, element):
        self.heap.append(element)
        self._heapify_up_iterative(len(self.heap) - 1)

    def _heapify_up_iterative(self, index):
        # Iterative approach using a stack to track parent indices
        stack = []
        while index != 0:
            parent_index = (index - 1) // 2
            stack.append(parent_index)
            if self.heap[parent_index] > self.heap[index]:
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                index = parent_index
            else:
                break

    def _heapify_down_iterative(self, index):
        while (index * 2 + 1) < len(self.heap):
            smallest_child_index = index * 2 + 1
            if (index * 2 + 2) < len(self.heap) and self.heap[index * 2 + 2] < self.heap[smallest_child_index]:
                smallest_child_index = index * 2 + 2
            if self.heap[index] > self.heap[smallest_child_index]:
                self.heap[index], self.heap[smallest_child_index] = self.heap[smallest_child_index], self.heap[index]
                index = smallest_child_index
            else:
                break

    def retrieve(self):
        if self.heap:
            value = self.heap[0]
            if len(self.heap) > 1:
                self.heap[0] = self.heap.pop() 
                self._heapify_down_iterative(0)
            else:
                self.heap.pop()
            return value
        return None

# Example usage
ih = IterativeHeap()
ih.insert(10)
ih.insert(20)
ih.insert(5)
print(ih.retrieve())  # Output: 5
print(ih.retrieve())  # Output: 10
print(ih.retrieve())  # Output: 20
