"""
You are given an m x n integer grid accounts where accounts[i][j] is the
amount of money the i-th customer has in the j-th bank.
Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank
accounts. The richest customer is the customer that has the maximum wealth.
"""


from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0
        for item in accounts:
            maximum = max(maximum, sum(item))
        return maximum


def main():
    accounts = [[1,5],[7,3],[3,5]]
    # [[1,5],[7,3],[3,5]]
    solution = Solution()
    print(solution.maximumWealth(accounts))


if __name__ == '__main__':
    main()
