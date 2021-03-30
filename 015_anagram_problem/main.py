def is_anagram_0(origin: str, possible_anagram: str):
    origin_list = list(origin)
    # brute-force
    for char in possible_anagram:
        try:
            origin_list.remove(char)
        except ValueError:
            return False

    if origin_list:
        return False
    return True


def is_anagram(origin: str, possible_anagram: str):

    if len(origin) != len(possible_anagram):
        return False

    origin_list = sorted(origin)
    possible_anagram_list = sorted(possible_anagram)
    # brute-force
    for index in range(len(origin_list)):
        if origin_list[index] != possible_anagram_list[index]:
            return False

    return True


if __name__ == '__main__':

    print(is_anagram('restful', 'fluster'))
    print(is_anagram('restful', 'fruster'))
