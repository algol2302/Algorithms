def reverse_string(s: str) -> str:
    """In-place solution"""
    data = list(s)
    start_index = 0
    end_index = len(s) - 1

    while end_index > start_index:
        data[start_index], data[end_index] = data[end_index], data[start_index]
        start_index += 1
        end_index -= 1

    return "".join(data)


def is_palindrome_0(s: str) -> bool:
    """Not in-place solution"""
    return s == s[::-1]


def is_palindrome(s: str) -> bool:
    """In-place solution"""
    reversed_string = reverse_string(s)
    return s == reversed_string


def main():
    print(is_palindrome("madam"))
    print(is_palindrome("cabin"))


if __name__ == '__main__':
    main()
