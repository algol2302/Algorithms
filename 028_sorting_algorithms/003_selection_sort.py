class SelectionSort:

    def __init__(self, nums):
        self.nums = nums

    def sort(self):

        # we make N-1 iterations
        # (N-1) * N = (N^2 - N) ~ N^2
        for i in range(len(self.nums)-1):
            # linear search and the index stores the index of the min item
            index = i

            # this is the linear search O(N)
            for j in range(i, len(self.nums)):
                # < - for ascending order
                # > - for descending order
                if self.nums[j] < self.nums[index]:
                    index = j

            # we have to swap the min item with the left-most item
            # we do not swap the item with itself
            if index != i:
                self.nums[index], self.nums[i] = self.nums[i], self.nums[index]


class RecursiveSelectionSort:

    def __init__(self, nums):
        self.nums = nums

    def min_index(self, start_index, finish_index):
        # linear search and the index stores the index of the min item

        if start_index == finish_index:
            return start_index

        index = start_index

        # this is the linear search O(N)
        for j in range(start_index, finish_index):
            # < - for ascending order
            # > - for descending order
            if self.nums[j] < self.nums[index]:
                index = j

        return index

    def selection_sort(self, start_index=0):
        if len(self.nums) == start_index:
            return

        min_index = self.min_index(start_index, len(self.nums))

        if min_index != start_index:
            self.nums[min_index], self.nums[start_index] = \
                self.nums[start_index], self.nums[min_index]

        start_index +=1

        self.selection_sort(start_index)

    def sort(self):
        self.selection_sort()

def main():
    # it has O(N^2) running time
    # algorithm = SelectionSort([1, -1, 0, 10, 12, -5, 1, 2, -1, 34])
    # algorithm.sort()
    # print(algorithm.nums)
    #
    # print('--------------------------')

    algorithm = RecursiveSelectionSort([1, -1, 0, 10, 12, -5, 1, 2, -1, 34])
    algorithm.sort()
    print(algorithm.nums)


if __name__ == '__main__':
    main()
