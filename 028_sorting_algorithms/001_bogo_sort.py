import random


class BogoSort:
    def __init__(self, nums):
        self.nums = nums

    def is_sorted(self):
        for i in range(len(self.nums) - 1):
            if self.nums[i] > self.nums[i + 1]:
                return False

        return True

    def shuffle(self):
        """Fisher-Yates approach:
        we generate a new permutation in O(N).
        It's in-place, so doesn't take any additional memory.
        """

        for i in range(len(self.nums) - 2, -1, -1):
            j = random.randint(0, i + 1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    def sort(self):

        while not self.is_sorted():
            print("Shuffle again")
            self.shuffle()


def main():

    # it has O(N!) running time
    algorithm = BogoSort([1, -1, 0, 10, 12, -5, 1, 2, -1, 34])
    algorithm.sort()
    print(algorithm.nums)


if __name__ == "__main__":
    main()
