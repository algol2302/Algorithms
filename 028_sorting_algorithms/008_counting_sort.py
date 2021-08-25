class CountingSort:

    def __init__(self, data):
        self.data = data
        # k = max - min + 1
        self.count_array = [0 for _ in range(max(data) - min(data) + 1)]

    def sort(self):
        # first we have to consider all the items in data in O(N) running time
        # indexes start with 0 + we should handle negative values as well
        for i in range(len(self.data)):
            self.count_array[self.data[i]-min(self.data)] += 1

        # we have to consider the counting array in O(k)
        z = 0
        for i in range(min(self.data), max(self.data)+1):
            while self.count_array[i - min(self.data)] > 0:
                self.data[z] = i
                z += 1
                self.count_array[i - min(self.data)] -= 1

def main():
    # it has O(N+k) running time and additional O(k) memory
    algorithm = CountingSort([1, -1, 0, 10, 12, -5, 1, 2, -1, 34])
    algorithm.sort()
    print(algorithm.data)


if __name__ == '__main__':
    main()
