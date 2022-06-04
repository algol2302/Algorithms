"""You are given a string s and an integer array indices of the same
length. The string s will be shuffled such that the character at the i-th
position moves to indices[i] in the shuffled string.

Return the shuffled string."""

from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        values = [""] * len(s)
        for i in range(len(s)):
            values[indices[i]] = s[i]
        return "".join(values)


def main():
    solution = Solution()

    print(
        solution.restoreString(s="codeleet", indices=[4, 5, 6, 7, 0, 2, 1, 3]),
        "leetcode",
    )
    print(
        solution.restoreString(s="abc", indices=[0, 1, 2]),
        "abc",
    )


if __name__ == "__main__":
    main()
