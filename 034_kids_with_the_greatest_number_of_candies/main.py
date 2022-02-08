"""There are n kids with candies. You are given an integer array
`candies`, where each candies[i] represents the number of candies the
i-th kid has, and an integer `extraCandies`, denoting the number of extra
candies that you have.

Return a boolean array result of length n, where result[i] is true if,
after giving the ith kid all the extraCandies, they will have the
greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies."""


from typing import List


class Solution:
    def kidsWithCandies(
        self, candies: List[int], extraCandies: int
    ) -> List[bool]:

        max_value = candies[0]
        res = []

        for item in candies[1:]:
            if item > max_value:
                max_value = item

        for item in candies:
            res.append(item + extraCandies >= max_value)

        return res


def main():
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3

    print(
        Solution().kidsWithCandies(candies=candies, extraCandies=extraCandies)
    )


if __name__ == "__main__":
    main()
