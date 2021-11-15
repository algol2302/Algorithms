class Solution:
    def algorithm(self, items: list[int]) -> int:
        max_sum = 0
        local_max = items[-1]

        for index in range(len(items)-1, -1, -1):
            max_sum += local_max
            if items[index-1] > local_max:
                local_max = items[index - 1]
        return max_sum

def main():
    items = [1, 2, 3, 4, 5]
    print(Solution().algorithm(items=items))


if __name__ == '__main__':
    main()
