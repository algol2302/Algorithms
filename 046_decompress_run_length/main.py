"""We are given a list nums of integers representing a list compressed
with run-length encoding.

Consider each adjacent pair of elements
[freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such
pair, there are freq elements with value val concatenated in a sublist.
Concatenate all the sublists from left to right to generate the
decompressed list.

Return the decompressed list."""


from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums), 2):
            res.extend([nums[i + 1]] * nums[i])
        return res


def main():
    print(Solution().decompressRLElist(nums=[1, 2, 3, 4]), [2, 4, 4, 4])
    print(Solution().decompressRLElist(nums=[1, 1, 2, 3]), [1, 3, 3])


if __name__ == "__main__":
    main()
