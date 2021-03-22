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


def longestPalindrome(s: str) -> str:
    """Optimized solution"""
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
                    max_length, items[current] = length_current, current

    return items.popitem()[0]


def main():
    print(f'got: {longestPalindrome("babad")}, expected: bab')
    print(f'got: {longestPalindrome("cbbd")}, expected: bb')
    print(f'got: {longestPalindrome("a")}, expected: a')
    print(f'got: {longestPalindrome("ac")}, expected: a')


if __name__ == '__main__':
    main()
