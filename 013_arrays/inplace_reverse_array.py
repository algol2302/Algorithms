def reverse(data: list) -> list:
    """In-place solution"""

    start_index = 0
    end_index = len(data) - 1

    while end_index > start_index:
        data[start_index], data[end_index] = data[end_index], data[start_index]
        start_index += 1
        end_index -= 1

    return data


def main():
    print(reverse([1, 2, 3, 4]))
    print(reverse([3, 0, -3]))


if __name__ == '__main__':
    main()
