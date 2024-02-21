class RecursiveHeap:
    def __init__(self):
        self.heap = []

    def insert(self, element):
        self.heap.append(element)
        self._heapify_up_recursive(len(self.heap) - 1)

    def _heapify_up_recursive(self, index):
        if index == 0:
            return
        parent_index = (index - 1) // 2
        if self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self._heapify_up_recursive(parent_index)

    def retrieve(self):
        if self.heap:
            value = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self._heapify_down_recursive(0)
            return value
        return None

    def _heapify_down_recursive(self, index):
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down_recursive(smallest)

# Example usage
rh = RecursiveHeap()
rh.insert(10)
rh.insert(20)
rh.insert(5)
print(rh.retrieve())  # Output: 5
print(rh.retrieve())  # Output: 10
print(rh.retrieve())  # Output: 20
