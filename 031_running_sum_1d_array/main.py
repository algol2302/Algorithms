"""
Given an array nums. We define a running sum of an array as
runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""

from typing import List


class Solution:
    def runningSum_0(self, nums: List[int]) -> List[int]:
        return [value + sum(nums[0:index]) for index, value in enumerate(nums)]

    def runningSum_1(self, nums: List[int]) -> List[int]:
        previous = 0
        res = []
        for index, item in enumerate(nums):
            res.append(previous + item)
            previous = res[index]
        return res

    def runningSum(self, nums: List[int]) -> List[int]:
        res = [nums[0]]
        for index in range(1, len(nums)):
            res.append(res[index - 1] + nums[index])
        return res


def main():
    nums = [1, 2, 3, 4]
    solution = Solution()
    print(solution.runningSum(nums))


if __name__ == "__main__":
    main()
