class InsertionSort:
    def __init__(self, nums):
        self.nums = nums

    def sort(self):
        for i in range(len(self.nums)):
            j = i

            # we have to check all previous items (not always all of them)
            # so in worst case we consider all previous items until J=0
            while j > 0 and self.nums[j - 1] > self.nums[j]:
                # swap items - shift operations
                # this is the main disadvantage of insertion sort
                self.nums[j - 1], self.nums[j] = self.nums[j], self.nums[j - 1]
                j -= 1


def main():
    # it has O(N^2) running time
    algorithm = InsertionSort([1, -1, 0, 10, 12, -5, 1, 2, -1, 34])
    algorithm.sort()
    print(algorithm.nums)


if __name__ == "__main__":
    main()
