def reverse_int_0(number: int) -> int:
    """Trivial solution"""
    return int(str(number)[::-1])


def reverse_int_1(number: int) -> int:
    reversed = 0

    while number > 0:
        remainder = number % 10
        reversed = reversed * 10 + remainder
        number = number // 10

    return reversed


def main():
    print(reverse_int_0(1234))
    print(reverse_int_0(9087))

    print(reverse_int_1(1234))
    print(reverse_int_1(9087))


if __name__ == '__main__':
    main()
