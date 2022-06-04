class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __gt__(self, other):
        return self.age > other.age

    def __repr__(self):
        return f"{self.name} - {self.age}"


def insetion_sort(persons: list[Person]):
    for i in range(len(persons)):
        j = i

        # we have to check all previous items (not always all of them)
        # so in worst case we consider all previous items until J=0
        while j > 0 and persons[j - 1] > persons[j]:
            # swap items - shift operations
            # this is the main disadvantage of insertion sort
            persons[j - 1], persons[j] = persons[j], persons[j - 1]
            j -= 1


def main():
    # it has O(N^2) running time
    persons = [Person("Alex", 10), Person("Bob", 22), Person("Alice", 5)]
    insetion_sort(persons)
    for person in persons:
        print(person)


if __name__ == "__main__":
    main()
