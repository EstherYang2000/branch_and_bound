class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, element):
        self.heap.append(element)
        self.heapify_up(len(self.heap) - 1)

    def delete(self):
        if not self.is_empty():
            self.swap(0, len(self.heap) - 1)
            self.heap.pop()
            self.heapify_down(0)

    def get_min(self):
        if not self.is_empty():
            return self.heap[0]
        else:
            return None

    def build_min_heap(self, elements):
        self.heap = elements
        n = len(self.heap)
        for i in range(n // 2, -1, -1):
            self.heapify_down(i)

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index].burst_time < self.heap[parent].burst_time:
                self.swap(index, parent)
                index = parent
            else:
                break

    def heapify_down(self, index):
        n = len(self.heap)
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < n and self.heap[left].burst_time < self.heap[smallest].burst_time:
            smallest = left

        if right < n and self.heap[right].burst_time < self.heap[smallest].burst_time:
            smallest = right

        if smallest != index:
            self.swap(index, smallest)
            self.heapify_down(smallest)


# # Example usage:
# if __name__ == '__main__':
#     min_heap = MinHeap()
#     elements = [4, 7, 1, 9, 3, 6]

#     min_heap.build_min_heap(elements)
#     print("Min heap:", min_heap.heap)

#     min_value = min_heap.get_min()
#     print("Min value:", min_value)

#     min_heap.delete()
#     print("Min heap after deleting root:", min_heap.heap)
