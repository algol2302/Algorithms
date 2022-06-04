from typing import Any


class HashTable:
    """Implementation of hash table with linear probing"""

    def __init__(self) -> None:
        # based on the load factor we may change the size of
        # the underlying data structure
        self.capacity = 10
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity

    def hash_function(self, key: str) -> int:
        """Non-perfect hash function"""

        hash_sum = 0

        for letter in key:
            hash_sum += ord(letter)

        return hash_sum % self.capacity

    def insert(self, key: str, data: Any) -> None:

        # we have to find a valid location for the value (data)
        index = self.hash_function(key)

        # there may be collisions which means that the index is already
        # occupied. while we do find an empty array slot
        while self.keys[index]:
            # sometimes we have to update the value if the key is already
            # present
            if self.keys[index] == key:
                self.values[index] = data
                return

            # do linear probing (try the next slot in the array)
            # because we may increment the index such that we are
            # outside the range of the underlying structure
            index = (index + 1) % self.capacity

        # we have found the valid slot for the item so we have to insert
        # the data
        self.keys[index] = key
        self.values[index] = data

    def get(self, key) -> [str, None]:

        # we have to find a valid location for the value (data)
        index = self.hash_function(key)

        while self.keys[index]:
            # this is when we find the item we are looking for
            if self.keys[index] == key:
                return self.values[index]

            index = (index + 1) % self.capacity

        # the given key value pair with key doesn't exists in the
        # hashtable
        return


def main():
    table = HashTable()

    table.insert("Adam", 23)
    table.insert("Kevin", 45)
    table.insert("Daniel", 34)
    table.insert("Daniel", 34)
    table.insert("Daniel", 33)

    print(table.get("Ana"))
    print(table.get("Adam"))
    print(table.get("Kevin"))
    print(table.get("Daniel"))


if __name__ == "__main__":
    main()
