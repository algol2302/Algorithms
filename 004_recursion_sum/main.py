import random


def recursive_sum(arr: list) -> int:

    if len(arr) == 1:
        return arr[0]

    elif len(arr) == 0:
        return 0

    else:
        return arr[0] + recursive_sum(arr=arr[1:])


if __name__ == '__main__':
    init_arr = [random.randint(0, 10) for _ in range(10)]
    total = recursive_sum(init_arr)
    checked = sum(init_arr)
    print(
        f"Initial values: {init_arr}\n"
        f"Sum: {total}\n"
        f"Verified: {total == checked}"
    )
