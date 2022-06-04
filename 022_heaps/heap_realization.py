CAPACITY = 10


class Heap:
    """Maximum heap (root node is the largest item)"""

    def __init__(self):
        # this is the actual number of items in the data structure
        self.heap_size: int = 0
        # the underlying list data structure
        self.heap = [0] * CAPACITY

    def insert(self, item):
        """O(logN) time complexity"""

        # when the heap is full
        if self.heap_size == CAPACITY:
            return

        self.heap[self.heap_size] = item
        self.heap_size += 1

        # check the heap properties
        self.fix_up(self.heap_size - 1)

    def fix_up(self, index: int):
        """
        starting with the actual node we have inserted up to root node
        we have to compare the values whether to make swap operations
        logN it has O(logN) time complexity
        """
        # i: 2*i+1=l 2i*2+2=r => i = (l-1)/2 = (r-2)/2
        parent_index = (index - 1) // 2

        # we consider all the items above till we hit the root node
        # if heap property is violated then we swap the parent-child
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = (
                self.heap[parent_index],
                self.heap[index],
            )
            self.fix_up(parent_index)

    def get_max(self):
        """peek() return with the max item in O(1)"""
        return self.heap[0]

    def poll(self):
        """
        return max and remove it as well
        remove root node of the heap
        O(logN) time complexity
        """
        max_item = self.get_max()

        # swap max item with the last item and "heapify":
        self.heap[0], self.heap[self.heap_size - 1] = (
            self.heap[self.heap_size - 1],
            self.heap[0],
        )
        self.heap_size -= 1

        # make sure that the heap is "heapify"
        self.fix_down(0)

        return max_item

    def fix_down(self, index: int):
        """
        starting with the root node downwards
        until the heap properties are no longer violated - O(logN)
        """

        left_index = 2 * index + 1
        right_index = 2 * index + 2

        # in a max heap the largest is always greater than the children
        largest_index = index

        # looking for the largest (parent or left node)
        if (
            left_index < self.heap_size
            and self.heap[left_index] > self.heap[index]
        ):
            largest_index = left_index

        # if the right child is greater than the left child:
        # largest us the right child
        if (
            right_index < self.heap_size
            and self.heap[right_index] > self.heap[largest_index]
        ):
            largest_index = right_index

        # if the parent is larger than the children: it's a valid heap
        # so we terminate the recursive function calls
        if index != largest_index:
            self.heap[index], self.heap[largest_index] = (
                self.heap[largest_index],
                self.heap[index],
            )
            self.fix_down(largest_index)

    def heap_sort(self):
        # we consider N items - it takes O(logN) to get max (poll function)
        # N * O(logN) = O(NlogN)
        for _ in range(self.heap_size):
            max_item = self.poll()
            print(max_item)


def main():
    heap = Heap()
    heap.insert(13)
    heap.insert(-2)
    heap.insert(0)
    heap.insert(8)
    heap.insert(1)
    heap.insert(-5)
    heap.insert(99)

    heap.heap_sort()


if __name__ == "__main__":
    main()
