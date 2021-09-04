"""
Given a zero-based permutation nums (0-indexed), build an array ans
of the same length where ans[i] = nums[nums[i]]
for each 0 <= i < nums.length and return it.

A zero-based permutation nums is an array of distinct integers
from 0 to nums.length - 1 (inclusive).
"""


from typing import List


class Solution:
    def buildArray_0(self, nums: List[int]) -> List[int]:
        return [nums[nums[index]] for index in range(len(nums))]

    def buildArray_1(self, nums: List[int]) -> List[int]:
        return [nums[item] for item in nums]

    def buildArray_2(self, nums: List[int]) -> List[int]:
        res = []
        for item in nums:
            res.append(nums[item])
        return res

    def buildArray(self, nums: List[int]) -> List[int]:
        return list(map(lambda x: nums[x], nums))


def main():
    nums = [0,2,1,5,3,4]
    print(Solution().buildArray(nums))


if __name__ == '__main__':
    main()
