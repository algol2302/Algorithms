"""Given the array nums, for each nums[i] find out how many numbers in
the array are smaller than it. That is, for each nums[i] you have to
count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

Example 1:
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation:
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1).
For nums[3]=2 there exist one smaller number than it (1).
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

Example 2:
Input: nums = [6,5,4,8]
Output: [2,1,0,3]

Example 3:
Input: nums = [7,7,7,7]
Output: [0,0,0,0]
"""

from typing import List


class Solution:
    def smallerNumbersThanCurrent_0(self, nums: List[int]) -> List[int]:
        res = []

        for i in nums:
            counter = 0
            for j in nums:
                if i != j and i > j:
                    counter += 1
            res.append(counter)

        return res

    def smallerNumbersThanCurrent_1(self, nums: List[int]) -> List[int]:
        """Not clear function but saves memory"""
        _sorted = sorted(nums)
        helper = {}
        # [8,1,2,2,3] -> [1,2,2,3,8]
        # [6,5,4,8] -> [4,5,6,8]
        # [7,7,7,7] -> [7,7,7,7]

        for index, item in enumerate(_sorted):
            helper.setdefault(item, index)

        for index, item in enumerate(nums):
            nums[index] = helper[item]

        return nums

    def smallerNumbersThanCurrent_2(self, nums: List[int]) -> List[int]:
        """Clear function but requires a bit more memory"""
        _sorted = sorted(nums)
        helper = {}

        for index, item in enumerate(_sorted):
            helper.setdefault(item, index)

        return [helper[item] for item in nums]


def main():
    for item, want in (
        ([8, 1, 2, 2, 3], [4, 0, 1, 1, 3]),
        ([6, 5, 4, 8], [2, 1, 0, 3]),
        ([7, 7, 7, 7], [0, 0, 0, 0]),
    ):
        print(Solution().smallerNumbersThanCurrent_2(item), "==", want)


if __name__ == "__main__":
    main()
