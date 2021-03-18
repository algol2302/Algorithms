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


def findMedianSortedArrays_0(nums1: List[int], nums2: List[int]) -> float:
    """n log(n) solution"""

    nums = nums1 + nums2
    nums = sorted(nums)
    n = len(nums)

    if n % 2 != 0:
        return float(nums[int(n / 2)])
    return float((nums[int((n - 1) / 2)] + nums[int(n / 2)]) / 2.0)


def findMedianSortedArrays(A: List[int], B: List[int]) -> float:
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, int((m + n + 1) / 2)
    while imin <= imax:
        i = int((imin + imax) / 2)
        j = half_len - i
        if i < m and B[j-1] > A[i]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and A[i-1] > B[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect

            if i == 0:
                max_of_left = B[j-1]
            elif j == 0:
                max_of_left = A[i-1]
            else:
                max_of_left = max(A[i-1], B[j-1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m:
                min_of_right = B[j]
            elif j == n:
                min_of_right = A[i]
            else:
                min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0


def main():
    nums1 = [1, 3]
    nums2 = [2]
    print(f"got: {findMedianSortedArrays(A=nums1, B=nums2)}, expected: {2.00000}")
    print("--------------------------")


if __name__ == '__main__':
    main()
