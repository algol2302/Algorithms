import random


def find_smallest(arr: list) -> int:
    smallest_index = 0
    smallest = arr[smallest_index]

    for index in range(1, len(arr)):
        if arr[index] < smallest:
            smallest = arr[index]
            smallest_index = index

    return smallest_index


def selection_sort(arr: list) -> list:
    new_arr = []

    for i in range(len(arr)):
        smallest_index = find_smallest(arr)
        new_arr.append(arr.pop(smallest_index))

    return new_arr


if __name__ == '__main__':
    rand_arr = [random.randint(0, 10) for i in range(10)]
    print(f"Random array:\t{rand_arr}")
    ordered_arr = selection_sort(rand_arr)
    print(f"Ordered:\t\t{ordered_arr}")
