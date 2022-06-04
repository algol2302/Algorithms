"""You are given a positive integer num consisting of exactly four
digits. Split num into two new integers new1 and new2 by using the digits
found in num. Leading zeros are allowed in new1 and new2, and all the
digits found in num must be used.

For example, given num = 2932, you have the following digits: two 2's,
one 9 and one 3. Some of the possible pairs [new1, new2]
are [22, 93], [23, 92], [223, 9] and [2, 329].
Return the minimum possible sum of new1 and new2.

Constraints:
    1000 <= num <= 9999
"""


class Solution:
    def minimumSum(self, num: int) -> int:
        values = [num % 10]
        for _ in range(3):
            num = num // 10
            values.append(num % 10)
        values = sorted(values)
        return (values[0] + values[1]) * 10 + values[2] + values[3]


def main():
    print(Solution().minimumSum(num=2932), 52)
    print(Solution().minimumSum(num=4009), 13)


if __name__ == "__main__":
    main()
