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
            res.extend((nums[index], nums[n + index]))
        return res

    def shuffle_1(self, nums: List[int], n: int) -> List[int]:
        # TODO in-place solution O(n) - time, 0(1) - space,
        #  I tried to use the math induction to derive formula for
        #  iterations and a bit stuck with it
        """
        x:
        index = 0,   nums[index] = index + 0         = index          = 0
        index = 1,   nums[index] = index + 1         = index + 1      = 2
        index = 2,   nums[index] = index + 1 + 1     = index + 2      = 4
        index = 3,   nums[index] = index + 1 + 1 + 1 = index + 3      = 6
        ...
        index = j,   nums[index] = j + 1 + 1 + ...   = j  + j         = 2j
        ...
        index = n-1, nums[index] = index + 1 + 1 +.. = index + n-2    = 2n-2

        y:
        index = n+0, nums[index] = index - n + 1       = index - n + 1= 1
        index = n+1, nums[index] = index - n + 1 + 1   = index - n + 2= 3
        index = n+2, nums[index] = index - n + 1 +1+1  = index - n + 3= 5
        ...
        index = n+i, nums[index] = index - n + 1 + i   = index - n+1+i= 2i+1
        ...
        index = 2n-2,nums[index] = index - n + 1 +.. = index - n +n-1 = 2n-3
        index = 2n-1,nums[index] = index - n + 1 +.. = index - n +n-0 = 2n-1

        """
        for old_index_x in range(0, n):
            new_index_x = 2 * old_index_x
            new_index_y = 2 * old_index_x + 1

            nums[new_index_x] = nums[old_index_x]
            nums[new_index_y] = nums[old_index_x + n]

        return nums

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # Let's apply divide & conquer approach:
        """
        n=1, [1,2] - do nothing

        n=2, [1,2,3,4] -> [1,3,2,4] ?: => [1,2<->3,4]

        n=3, [1,2,3,4,5,6] -> [1,4,2,5,3,6] ?: =>
            1. [1,2,3<->4,5,6]->[1,2,4,3,5,6]
            2. [1,2<->4,3<->5,6]->[1,4,2,5,3,6]

        n=4, [1,2,3,4,5,6,7,8]->[1,4,2,6,3,7,4,8] ?:
            1. [1,2,3,4<->5,6,7,8]->[1,2,3,5,4,6,7,8]
            2. [1,2,3<->5,4<->6,7,8]->[1,2,5,3,6,4,7,8]
            3. [1,2<->5,3<->6,4<->7,8]->[1,4,2,6,3,7,4,8] !!!

        n=5, [1,2,3,4,5,6,7,8,9,10]->[1,6,2,7,3,8,4,9,5,10] ?:
            1. [1,2,3,4,5<->6,7,8,9,10]->[1,2,3,4,6,5,7,8,9,10]
            2. [1,2,3,4<->6,5<->7,8,9,10]->[1,2,3,6,4,7,5,8,9,10]
            3. [1,2,3<->6,4<->7,5<->8,9,10]->[1,2,6,3,7,4,8,5,9,10]
            4. [1,2<->6,3<->7,4<->8,5<->9,10]->[1,6,2,7,3,8,4,9,5,10]
        """

        # if n == 1:
        #     return nums
        #
        # if n == 2:
        #     # 1.
        #     nums[1], nums[2] = nums[2], nums[1]
        #     return nums

        # if n == 3:
        #     # 1.
        #     nums[2], nums[3] = nums[3], nums[2]
        #     # 2.
        #     nums[1], nums[2] = nums[2], nums[1]
        #     nums[3], nums[4] = nums[4], nums[3]

        # if n == 4:
        #     # 1.
        #     nums[3], nums[4] = nums[4], nums[3]
        #     # 2.
        #     nums[2], nums[3] = nums[3], nums[2]
        #     nums[4], nums[5] = nums[5], nums[4]
        #     # 3.
        #     nums[1], nums[2] = nums[2], nums[1]
        #     nums[3], nums[4] = nums[4], nums[3]
        #     nums[5], nums[6] = nums[6], nums[5]

        for idx, i in enumerate(range(n - 1, 0, -1), start=1):
            for j in range(0, 2 * idx, 2):
                nums[i + j], nums[i + j + 1] = nums[i + j + 1], nums[i + j]
        return nums


def main():
    nums = [1, 2, 3, 4, 5, 6]
    n = 3
    solution = Solution()
    print(solution.shuffle(nums, n))


if __name__ == "__main__":
    main()
