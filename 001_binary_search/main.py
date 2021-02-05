from typing import Optional


def binary_search(array: list, item: int) -> Optional[int]:
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = round((low + high) / 2)
        guess = array[mid]

        if guess == item:
            return mid

        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


if __name__ == '__main__':
    print(binary_search([-1, 1, 3, 4, 5, 6, 7], -1))
