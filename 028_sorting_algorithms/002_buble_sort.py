class BubbleSort:
    def __init__(self, nums):
        self.nums = nums

    def sort(self):
        for i in range(len(self.nums) - 1):
            for j in range(len(self.nums) - i - 1):
                if self.nums[j] > self.nums[j + 1]:
                    self.nums[j], self.nums[j + 1] = (
                        self.nums[j + 1],
                        self.nums[j],
                    )


def main():
    # it has O(N^2) running time
    algorithm = BubbleSort([1, -1, 0, 10, 12, -5, 1, 2, -1, 34])
    algorithm.sort()
    print(algorithm.nums)


if __name__ == "__main__":
    main()
