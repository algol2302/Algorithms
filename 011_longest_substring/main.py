def lengthOfLongestSubstring1(s: str) -> int:
    """Sliding window solution with index detection inside of loop"""
    max_length = 0
    current = []

    for char in s:

        if char in current:
            first_index = current.index(char)
            current = current[first_index+1:]

        current.append(char)

        max_length = max(max_length, len(current))

    return max_length


def lengthOfLongestSubstring2(s: str) -> int:
    """Sliding window solution with index detection via hashmap"""

    max_length = 0
    current = ''
    items = {}

    for index, char in enumerate(s):
        if char in current:
            current = s[items[char]+1:index]

        items[char] = index
        current += char

        max_length = max(max_length, len(current))

    return max_length


def main():
    lengthOfLongestSubstring = lengthOfLongestSubstring2

    # Input: s = "abcabcbb"
    Output: 3
    s = "abcabcbb"
    print(f"{s=}\tgot: {lengthOfLongestSubstring(s)} expected: 3")

    # Input: s = "bbbbb"
    # Output: 1
    s = "bbbbb"
    print(f"{s=}\t\tgot: {lengthOfLongestSubstring(s)} expected: 1")

    # Input: s = "pwwkew"
    # Output: 3
    s = "pwwkew"
    print(f"{s=}\t\tgot: {lengthOfLongestSubstring(s)} expected: 3")

    # Input: s = ""
    # Output: 0
    s = ""
    print(f"{s=}\t\t\tgot: {lengthOfLongestSubstring(s)} expected: 0")

    # Input: s = "dvdf"
    s = "dvdf"
    # Expected: 3
    print(f"{s=}\t\t\tgot: {lengthOfLongestSubstring(s)} expected: 3")

    s = "tmmzuxt"
    # Expected: 3
    print(f"{s=}\t\tgot: {lengthOfLongestSubstring(s)} expected: 5")

    s = "aabaab!bb"
    # Expected: 3
    print(f"{s=}\t\tgot: {lengthOfLongestSubstring(s)} expected: 3")

    s = "bbtablud"
    print(f"{s=}\t\tgot: {lengthOfLongestSubstring(s)} expected: 6")


if __name__ == '__main__':
    main()
