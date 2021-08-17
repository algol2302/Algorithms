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

def main():
    # it has O(N^2) running time
    algorithm = SelectionSort([1, -1, 0, 10, 12, -5, 1, 2, -1, 34])
    algorithm.sort()
    print(algorithm.nums)


if __name__ == '__main__':
    main()
