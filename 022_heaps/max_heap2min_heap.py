from is_min_heap import is_min_heap_optimized


class HeapTransformer:
    def __init__(self, heap: list) -> None:
        self.heap = heap

    def transform(self) -> None:
        for index in range((len(self.heap) - 2) // 2, -1, -1):
            self.fix_down(index)

    def fix_down(self, index: int) -> None:
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        # in a max heap the largest is always greater than the children
        largest_index = index

        # looking for the min (parent or left node)
        if left_index < len(self.heap) and self.heap[left_index] < self.heap[index]:
            largest_index = left_index

        # if the right child is smaller than the left child:
        # min is the right child
        if right_index < len(self.heap) and self.heap[right_index] < self.heap[largest_index]:
            largest_index = right_index

        # if the parent is larger than the children: it's a valid heap
        # so we terminate the recursive function calls
        if index != largest_index:
            self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
            self.fix_down(largest_index)


def main():
    heap = [210, 100, 23, 2, 5]
    heap_tranform = HeapTransformer(heap)
    heap_tranform.transform()
    print(heap_tranform.heap)
    print(f"is the min heap: {is_min_heap_optimized(heap_tranform.heap)}")


if __name__ == '__main__':
    main()
