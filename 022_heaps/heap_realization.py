CAPACITY = 10


# maximum heap (root node is the largest item)
class Heap:

    def __init__(self):
        # this is the actual number of items in the data structure
        self.heap_size: int = 0
        # the underlying list data structure
        self.heap = [0] * CAPACITY

    def insert(self, item):

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
            self.heap[index], self.heap[parent_index] = \
                self.heap[parent_index], self.heap[index]
            self.fix_up(parent_index)

    def get_max(self):
        """peek() return with the max item in O(1)"""
        return self.heap[0]

    def poll(self):
        """
        return max and remove it as well
        remove root node of the heap
        """
        max_item = self.get_max()

        # swap max item with the last item and "heapify":
        self.heap[0], self.heap[self.heap_size - 1] = \
            self.heap[self.heap_size - 1], self.heap[0]

        # make sure that the heap is "heapify"
        self.fix_down(self.heap[0])

        return max_item

    def fix_dowm(self, index: int):
        """
        starting with the root node downwards
        until the heap properties are no longer violated - O(logN)
        """

        left_index = 2 * index + 1
        right_index = 2 * index + 2

        # in a max heap the largest is always greater than the children
        largest_index = index

        # looking for the largest (parent or left node)
        if left_index < self.heap_size and \
                self.heap[left_index] > self.heap[index]:
            largest_index = left_index

        # if the right child is greater than the left child:
        # largest us the right child
        if right_index > self.heap_size and \
                self.heap[right_index] > self.heap[index]:
            largest_index = right_index

        # if the parent is larger than the children: it's a valid heap
        # so we terminate the recursive function calls
        if index != largest_index:
            self.heap[index], self.heap[largest_index] = \
                self.heap[largest_index], self.heap[index]
            self.fix_dowm(largest_index)


def main():
    pass


if __name__ == '__main__':
    main()
