def is_palindrome(s: str) -> bool:
    """Not in-place solution"""
    return s == s[::-1]


def main():
    print(is_palindrome("madam"))
    print(is_palindrome("cabin"))


if __name__ == '__main__':
    main()
