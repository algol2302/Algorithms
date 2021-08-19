class ShellSort:

    def __init__(self, nums):
        self.nums = nums

    def sort(self):

        gap = len(self.nums) // 2

        while gap > 0:

            # this is the same as insertion sort but here we have to
            # consider items that are as far away from each other as
            # the value of the 'gap'
            for i in range(gap, len(self.nums)):
                j = i
                while j >= gap and self.nums[j - gap] > self.nums[j]:
                    self.nums[j - gap], self.nums[j] = \
                        self.nums[j], self.nums[j - gap]
                    j -= gap

            gap = gap // 2


def main():
    # it has O(N^2) running time
    algorithm = ShellSort([1, -1, 0, 10, 12, -5, 1, 2, -1, 34])
    algorithm.sort()
    print(algorithm.nums)


if __name__ == '__main__':
    main()
