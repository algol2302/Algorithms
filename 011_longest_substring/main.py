def lengthOfLongestSubstring(s: str) -> int:
    longest = set()
    current = []

    for char in s:
        # TODO
        current.append(char)
        if len(longest) <= len(current) and "".join(current) in s:
            longest.update(current)
        else:
            current = []

    print(longest)

    return len(longest)


def main():
    # Input: s = "abcabcbb"
    # Output: 3
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


if __name__ == '__main__':
    main()
