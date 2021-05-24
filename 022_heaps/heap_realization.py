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

    # starting with the actual node we have inserted up to root node
    # we have to compare the values whether to make swap operations
    # logN it has O(logN) time complexity
    def fix_up(self, arg: int):
        pass


def main():
    pass


if __name__ == '__main__':
    main()
