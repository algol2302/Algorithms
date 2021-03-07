from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """Brute-force solution"""
    for first_index, first in enumerate(nums):
        for second_index, second in enumerate(nums):

            if first_index == second_index:
                continue

            if (first + second) == target:
                return [first_index, second_index]

    return []


def two_sum_optimized_1(nums: List[int], target: int) -> List[int]:
    """First optimization"""

    for first_index, first in enumerate(nums):
        for second_index, second in enumerate(nums[first_index+1:], start=first_index+1):
            if target - first == second:
                return [first_index, second_index]

    return []


def two_sum_optimized_2(nums: List[int], target: int) -> List[int]:
    """Second optimization"""

    _helper = {}
    for first_index, key in enumerate(nums):
        second = target - key

        try:
            if first_index != _helper[key]:
                return [first_index, _helper[key]]
        except KeyError:
            pass

        _helper[second] = first_index

    return []


def main():
    print(two_sum_optimized_1([2, 7, 11, 15], 9))
    print(two_sum_optimized_1([3, 2, 4], 6))
    print(two_sum_optimized_1([3, 3], 6))
    print(two_sum_optimized_1([1, 3, 4, 2], 6))

    print('--------')

    print(two_sum_optimized_2([2, 7, 11, 15], 9))
    print(two_sum_optimized_2([3, 2, 4], 6))
    print(two_sum_optimized_2([3, 3], 6))
    print(two_sum_optimized_2([1, 3, 4, 2], 6))


if __name__ == '__main__':
    main()
