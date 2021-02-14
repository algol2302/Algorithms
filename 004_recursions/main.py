import random


def recursive_sum(arr: list) -> int:
    if len(arr) == 1:
        return arr[0]
    return arr[0] + recursive_sum(arr=arr[1:])


def recursive_count(arr: list) -> int:
    if len(arr) == 0:
        return 0
    return 1 + recursive_count(arr=arr[1:])


def recursive_max(arr: list) -> int:
    if len(arr) == 0:
        raise ValueError('recursive_max() arg is an empty sequence')

    if len(arr) == 1:
        return arr[0]

    rest = recursive_max(arr=arr[1:])

    return rest if rest > arr[0] else arr[0]


def quick_sort(arr: list):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(arr=less) + [pivot] + quick_sort(arr=greater)


if __name__ == '__main__':
    init_arr = [random.randint(0, 1000) for _ in range(10)]

    total_sum = recursive_sum(init_arr)
    total_count = recursive_count(init_arr)
    max_value = recursive_max(init_arr)
    q_sorted = quick_sort(init_arr)

    print(
        f"Initial values:\t{init_arr}\n"
        f"Sorted:\t\t\t{q_sorted} check: {q_sorted == sorted(init_arr)}\n"
        f"Sum: {total_sum}\t\tcheck: {total_sum == sum(init_arr)}\n"
        f"Count: {total_count}\t\tcheck: {total_count == len(init_arr)}\n"
        f"Max: {max_value}\t\tcheck: {max_value == max(init_arr)}\n"
    )
