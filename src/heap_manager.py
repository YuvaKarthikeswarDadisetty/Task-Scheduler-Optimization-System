import heapq


class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, task):
        heapq.heappush(self.heap, (-task.profit, task))

    def pop(self):
        if not self.is_empty():
            return heapq.heappop(self.heap)[1]
        return None

    def peek(self):
        if not self.is_empty():
            return self.heap[0][1]
        return None

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def get_all_tasks(self):
        return [item[1] for item in self.heap]


def build_heap_from_tasks(tasks):
    heap = MaxHeap()
    for task in tasks:
        heap.push(task)
    return heap


def display_heap(heap):
    print("\n🔥 Heap Contents:")
    print("-" * 60)
    for item in heap.heap:
        print(item[1])
    print("-" * 60)