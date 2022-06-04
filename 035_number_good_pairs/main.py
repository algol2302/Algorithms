"""Given an array of integers nums, return the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j."""

from typing import List


class Solution:
    def numIdenticalPairs_0(self, nums: List[int]) -> int:
        """Leetcode, why do you use camelCase in python?"""
        counter = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    counter += 1
        return counter

    def numIdenticalPairs_1(self, nums: List[int]) -> int:
        counter_dict = {}
        counter = 0

        for item in nums:
            if counter_dict.get(item):
                counter_dict[item] += 1
            else:
                counter_dict[item] = 1

        for value in counter_dict.values():
            counter += value * (value - 1) // 2

        return counter


def main():
    nums = [1, 2, 3, 1, 1, 3]

    print(Solution().numIdenticalPairs_1(nums=nums))


if __name__ == "__main__":
    main()
