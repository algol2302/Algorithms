class MergeSort:

    def __init__(self, nums):
        self.nums = nums

    def sort(self):
        self.merge_sort(self.nums)

    @classmethod
    def merge_sort(cls, nums):
        # define base case: that we keep splitting the lists until
        # the sub-lists have just 1 items - arrays will a single item
        # is sorted by default
        if len(nums) == 1:
            return

        # divide phase:
        middle_index = len(nums) // 2
        left_half = nums[:middle_index]
        right_half = nums[middle_index:]

        cls.merge_sort(left_half)
        cls.merge_sort(right_half)

        # conquer phase:
        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            # > - for descending order:
            # < - for ascending order:
            if left_half[i] < right_half[j]:
                nums[k] = left_half[i]
                i += 1
            else:
                nums[k] = right_half[j]
                j += 1

            k += 1

        # after that there may be additional items in the left
        # (right) subarray
        while i < len(left_half):
            nums[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            nums[k] = right_half[j]
            j += 1
            k += 1


def main():
    # it has O(NxLogN) running time and additional O(N) memory
    algorithm = MergeSort([1, -1, 0, 10, 12, -5, 1, 2, -1, 34])
    algorithm.sort()
    print(algorithm.nums)


if __name__ == '__main__':
    main()
