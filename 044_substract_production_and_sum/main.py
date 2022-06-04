"""Given an integer number n, return the difference between the product
of its digits and the sum of its digits."""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sum = 0
        while n:
            digit = n % 10
            prod *= digit
            sum += digit
            n = n // 10
        return prod - sum


def main():
    print(Solution().subtractProductAndSum(n=234), 15)
    print(Solution().subtractProductAndSum(n=4421), 21)


if __name__ == "__main__":
    main()
