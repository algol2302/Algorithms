from typing import List


class Solution:
    def mostWordsFound_0(self, sentences: List[str]) -> int:
        res = 0
        for item in sentences:
            res = max(res, len(item.split(" ")))
        return res

    def mostWordsFound_1(self, sentences: List[str]) -> int:
        res = 0
        for item in sentences:
            res = max(res, item.count(" "))
        return res


def main():
    pass


if __name__ == "__main__":
    main()
