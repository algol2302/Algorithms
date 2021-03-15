"""
Definition: https://www.geeksforgeeks.org/program-for-mean-and-median-of-an-unsorted-array/

Median of a sorted array of size n is defined as the middle element when n is odd and average of middle two elements when n is even.
Since the array is not sorted here, we sort the array first, then apply above formula.

Examples:

Input  : a[] = {1, 3, 4, 2, 6, 5, 8, 7}
Output : Mean = 4.5
         Median = 4.5
Sum of the elements is 1 + 3 + 4 + 2 + 6 +
5 + 8 + 7 = 36
Mean = 36/8 = 4.5
Since number of elements are even, median
is average of 4th and 5th largest elements.
which means (4 + 5)/2 = 4.5

Input  : a[] = {4, 4, 4, 4, 4}
Output : Mean = 4
         Median = 4
"""

from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    """n log(n) solution"""

    nums = nums1 + nums2
    nums = sorted(nums)
    n = len(nums)

    if n % 2 != 0:
        return float(nums[int(n / 2)])
    return float((nums[int((n - 1) / 2)] + nums[int(n / 2)]) / 2.0)


def main():
    nums1 = [1, 3]
    nums2 = [2]
    print(f"got: {findMedianSortedArrays(nums1=nums1, nums2=nums2)}, expected: {2.00000}")
    print("--------------------------")


if __name__ == '__main__':
    main()
