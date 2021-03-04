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


def main():
    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([3, 2, 4], 6))
    print(two_sum([3, 3], 6))


if __name__ == '__main__':
    main()
