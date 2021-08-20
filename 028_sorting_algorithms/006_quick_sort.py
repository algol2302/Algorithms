class QuickSort:

    def __init__(self, data):
        self.data = data

    def sort(self):
        self.quick_sort(0, len(self.data)-1)

    # low is the index of the first item
    # high is the index of the last item
    def quick_sort(self, low: int, high: int):

        if low >= high:
            return

        pivot_index = self.partition(low, high)
        # call the function recursively on the left array:
        self.quick_sort(low, pivot_index-1)
        # call the function recursively on the right array:
        self.quick_sort(pivot_index+1, high)

    # this is the magic happens
    # in O(N) running time complexity
    def partition(self, low: int, high: int):

        # we use the middle item as the pivot
        # or we can use random index
        pivot_index = (low + high) // 2

        # swap items:
        self.data[pivot_index], self.data[high] = \
            self.data[high], self.data[pivot_index]

        # consider all the other items and compare them with the pivot
        for j in range(low, high):
            if self.data[j] <= self.data[high]:
                self.data[low], self.data[j] = self.data[j], self.data[low]
                low += 1

        # we have considered all the items - we have to swap the pivot
        # and the low:
        self.data[low], self.data[high] = self.data[high], self.data[low]

        # return the index the pivot
        return low

def main():
    # it has O(NxlogN) running time
    algorithm = QuickSort([1, -1, 0, 10, 12, -5, 1, 2, -1, 34])
    algorithm.sort()
    print(algorithm.data)


if __name__ == '__main__':
    main()
