from collections import deque
from typing import Any
from pprint import pprint


graph = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}


class Graph:
    def __init__(self, name: str, is_mango_seller: bool, friends: Any) -> None:
        self.name = name
        self.is_mango_seller = is_mango_seller
        self.friends = friends

    def _as_dict(self) -> dict:
        return {
            "name": self.name,
            "is_mango_seller": self.is_mango_seller,
            "friends": self.friends
        }

    def __repr__(self):
        return f"Graph({self._as_dict()!r})"


graph2 = Graph(
    name="you",
    is_mango_seller=False,
    friends=(
        Graph(
            name="alice",
            is_mango_seller=False,
            friends=None
        ),
        Graph(
            name="bob",
            is_mango_seller=False,
            friends=None
        ),
        Graph(
            name="claire",
            is_mango_seller=False,
            friends=None
        )
    )
)

def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person, "is а mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)

    return False


if __name__ == '__main__':
    pprint(graph2._as_dict())
    pprint(graph)

    search("you")
