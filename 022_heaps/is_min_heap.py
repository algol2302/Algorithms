"""In a min heap the parent is smaller than the children"""


def is_min_heap(heap: list) -> bool:
    """A brute-force realization"""

    # i: 2*i+1=l 2i*2+2=r => i = (l-1)/2 = (r-2)/2
    for index in range(1, len(heap) - 1):
        parent_index = (index - 1) // 2
        if heap[parent_index] >= heap[index]:
            return False

    return True


def is_min_heap_optimized(heap: list) -> bool:
    """An optimized realization"""

    # there is not need to check the leaf nodes:
    num_items = (len(heap) - 2) // 2
    # i: 2*i+1=l 2i*2+2=r => i = (l-1)/2 = (r-2)/2
    for index in range(num_items):
        if (
            heap[index] > heap[2 * index + 1]
            or heap[index] > heap[2 * index + 2]
        ):
            return False

    return True


def main():
    is_not_min_heap = [4, 7, 3, -2, 1, 0]
    is_true_min_heap1 = [-2, 1, 0, 7, 4, 3]
    is_true_min_heap2 = [-2, 1, 0, 7, 3, 4]

    assert is_min_heap(is_true_min_heap1) == True
    assert is_min_heap(is_true_min_heap2) == True
    assert is_min_heap(is_not_min_heap) == False

    assert is_min_heap_optimized(is_true_min_heap1) == True
    assert is_min_heap_optimized(is_true_min_heap2) == True
    assert is_min_heap_optimized(is_not_min_heap) == False


if __name__ == "__main__":
    main()
