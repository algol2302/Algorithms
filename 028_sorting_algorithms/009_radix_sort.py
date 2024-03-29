import random

ITEMS_IN_BUCKET = 10


class RadixSort:
    def __init__(self, data):
        self.data = data

    def get_digits(self):
        return len(str(max(self.data)))

    def counting_sort(self, d):
        count_array = [[] for _ in range(ITEMS_IN_BUCKET)]

        # store the count of each element in count array O(N)
        for num in self.data:
            # calculate index of the given bucket
            index = (num // (10**d)) % 10
            count_array[index].append(num)

        # we have to consider all the items in the count array (list)
        z = 0
        for i in range(len(count_array)):
            while len(count_array[i]) > 0:
                # it takes O(N) linear running time complexity - dictionary O(1)
                self.data[z] = count_array[i].pop(0)
                z += 1

    def sort(self):
        for digit in range(self.get_digits()):
            self.counting_sort(digit)


def main():
    # [1, -1, 0, 10, 12, -5, 1, 2, -1, 34]
    n = [5, 3, 10, 12, 9, 8, 20, 100, 325, 1023]
    random.shuffle(n)
    print(n)
    algorithm = RadixSort(n)
    algorithm.sort()
    print(algorithm.data)


if __name__ == "__main__":
    main()
