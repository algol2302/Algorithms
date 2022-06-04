"""Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2,
otherwise, you have to subtract 1 from it."""


class Solution:
    def numberOfSteps0(self, num: int) -> int:
        counter = 0
        while num:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            counter += 1
        return counter

    def numberOfSteps1(self, num: int) -> int:
        digits = f"{num:b}"
        return digits.count("1") - 1 + len(digits)


def main():
    print(
        Solution().numberOfSteps1(num=14), 6
    )
    print(Solution().numberOfSteps1(num=8), 4)
    print(Solution().numberOfSteps1(num=123), 12)


if __name__ == "__main__":
    main()
