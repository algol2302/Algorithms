"""
Given the array nums consisting of 2n elements in the form
[x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""


from typing import List


class Solution:
    def shuffle_0(self, nums: List[int], n: int) -> List[int]:
        res = []
        for index in range(0, n):
            res.extend((nums[index], nums[n+index]))
        return res

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # TODO in-place solution O(n) - time, 0(1) - space
        for index in range(1, n, 3):
            nums[index], nums[index+1], nums[n+index-1] = nums[n+index-1], nums[index], nums[index+1]
        return nums


def main():
    nums = [1,2,3,4,4,3,2,1]
    n = 4
    solution = Solution()
    print(solution.shuffle(nums, n))


if __name__ == '__main__':
    main()
