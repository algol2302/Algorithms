def find_duplicates_0(values: list) -> list:
    """Should be O(N) time complexity"""
    duplicates = []
    # + O(N) for space complexity
    check = {}

    for item in values:
        if not check.get(item):
            check[item] = item
        else:
            duplicates.append(item)
    return duplicates


def find_duplicates(values: list) -> list:
    """Should be O(N) time complexity.
    Values are positive and less than len(values)
    """
    duplicates = []

    for item in values:
        if values[abs(item)] >= 0:
            values[abs(item)] = -values[abs(item)]
        else:
            duplicates.append(abs(item))
    return duplicates


def main():
    print(find_duplicates([1, 2, 3, 1, 4]))
    print(find_duplicates([2, 3, 1, 2, 3]))


if __name__ == "__main__":
    main()
