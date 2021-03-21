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

    # TODO optimize it )

    palindrom = ''
    items = {}

    for i, char_i in enumerate(s):
        current = char_i

        if len(palindrom) < len(current) and current == current[::-1]:
            palindrom = current

        for j, char_j, in enumerate(s[i+1:]):
            current += char_j

            if len(palindrom) < len(current) and current == current[::-1]:
                palindrom = current

    return palindrom


def main():
    print(f'got: {longestPalindrome("babad")}, expected: bab')
    print(f'got: {longestPalindrome("cbbd")}, expected: bb')
    print(f'got: {longestPalindrome("a")}, expected: a')
    print(f'got: {longestPalindrome("ac")}, expected: a')


if __name__ == '__main__':
    main()
