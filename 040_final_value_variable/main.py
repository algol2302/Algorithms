"""
There is a programming language with only four operations and one
variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations,
return the final value of X after performing all the operations.
"""
from typing import List


class Solution:
    def finalValueAfterOperations_0(self, operations: List[str]) -> int:
        operation_helper = {
            "++X": lambda x: x + 1,
            "X++": lambda x: x + 1,
            "--X": lambda x: x - 1,
            "X--": lambda x: x - 1,
        }

        x = 0
        for item in operations:
            x = operation_helper[item](x)
        return x

    def finalValueAfterOperations_1(self, operations: List[str]) -> int:
        operation_helper = {
            "++X": 1,
            "X++": 1,
            "--X": -1,
            "X--": -1,
        }

        x = 0
        for item in operations:
            x += operation_helper[item]
        return x


def main():
    # operations = ["--X", "X++", "X++"] -> 1
    # operations = ["++X","++X","X++"] -> 3
    # operations = ["X++","++X","--X","X--"] -> 0
    for item in (
        ["--X", "X++", "X++"], ["++X","++X","X++"], ["X++","++X","--X","X--"]
    ):
        print(Solution().finalValueAfterOperations_1(item))


if __name__ == '__main__':
    main()
