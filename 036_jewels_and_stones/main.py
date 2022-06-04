"""You're given strings jewels representing the types of stones that are
jewels, and stones representing the stones you have. Each character in stones
is a type of stone you have. You want to know how many of the stones you have
are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone
from "A"."""


class Solution:
    def numJewelsInStones_0(self, jewels: str, stones: str) -> int:
        """Brute-force"""

        counter = 0
        for jewel in jewels:
            for stone in stones:
                if jewel == stone:
                    counter += 1
        return counter

    def numJewelsInStones_1(self, jewels: str, stones: str) -> int:
        counter = 0
        for stone in stones:
            counter += stone in jewels
        return counter

    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0
        d = {}
        for jewel in jewels:
            d[jewel] = 1

        for stone in stones:
            if d.get(stone):
                counter += 1
        return counter


def main():
    jewels = "aA"
    stones = "aAAbbbb"

    print(Solution().numJewelsInStones(jewels=jewels, stones=stones))


if __name__ == "__main__":
    main()
