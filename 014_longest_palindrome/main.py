def longestPalindrome_0(s: str) -> str:
    """Brute force solution"""

    palindrom = ''

    for i, char_i in enumerate(s):
        current = char_i

        if len(palindrom) < len(current) and current == current[::-1]:
            palindrom = current

        for j, char_j, in enumerate(s[i+1:]):
            current += char_j

            if len(palindrom) < len(current) and current == current[::-1]:
                palindrom = current

    return palindrom


def longestPalindrome_1(s: str) -> str:
    """Optimized solution 1"""
    length_s = len(s)

    if length_s == 1:
        return s[0]

    if length_s == 2:
        if s[0] == s[1]:
            return s
        return s[0]

    max_length = 1
    items = {s[0]: 1}

    for i in range(0, length_s):
        current = s[i]

        for j, char_j in enumerate(s[i+1:]):
            current += char_j
            length_current = len(current)

            try:
                items[current]
            except KeyError:
                if max_length < length_current and current == current[::-1]:
                    max_length, items[current] = length_current, length_current

    return items.popitem()[0]


def longestPalindrome_2(s: str) -> str:
    """Optimized solution 2"""
    length_s = len(s)

    max_length = 1
    items = {}
    max_palindrom = s[0]

    for i in range(0, length_s):
        current = s[i]

        for j, char_j in enumerate(s[i+1:]):
            current += char_j
            length_current = len(current)

            try:
                items[current]
            except KeyError:
                items[current] = current == current[::-1]

            if max_length < length_current and items[current]:
                max_length, max_palindrom = length_current, current

    return max_palindrom


def longestPalindrome_3(s: str) -> str:
    """Optimized solution 3"""
    length_s = len(s)

    max_length = 1
    items = {}
    max_palindrom = s[0]

    for i in range(0, length_s):
        current = s[i]

        for char_j in s[i+1:]:
            current += char_j

            try:
                if max_length < items[current][1] and items[current][0]:
                    max_length, max_palindrom = items[current][1], current
            except KeyError:
                items[current] = (current == current[::-1], len(current))
                if max_length < items[current][1] and items[current][0]:
                    max_length, max_palindrom = items[current][1], current

    return max_palindrom


def longestPalindrome_4(s: str) -> str:
    """Optimized solution 4 from leetcode"""

    if len(s) == 2 and s[0] != s[1]:
        return s[0]

    if s == s[::-1]:
        return s

    i = 0
    b = len(s) - 1
    j = 1

    while s[i:b] != s[i:b][::-1]:
        i += 1
        b += 1

        if b == len(s) + 1:
            i = 0
            j += 1
            b = len(s) - j
    return s[i:b]


def longestPalindrome(s: str) -> str:
    """Optimized solution 5 from leetcode"""

    length = len(s)

    def get_max_len(string: str, left: int, right: int) -> int:
        while left >= 0 and right < length and string[left] == string[right]:
            left -= 1
            right += 1
        return right - left - 1

    start = end = 0

    for i in range(length):
        max_len_1 = get_max_len(s, i, i + 1)
        max_len_2 = get_max_len(s, i, i)
        max_len = max(max_len_1, max_len_2)
        if max_len > end - start + 1:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    return s[start: end + 1]


def main():
    print(f'got: {longestPalindrome("babad")}, expected: bab')
    print(f'got: {longestPalindrome("cbbd")}, expected: bb')
    print(f'got: {longestPalindrome("a")}, expected: a')
    print(f'got: {longestPalindrome("ac")}, expected: a')


if __name__ == '__main__':
    main()
