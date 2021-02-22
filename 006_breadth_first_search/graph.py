from typing import Any
from pprint import pprint


class Graph:
    # TODO realize graph class:
    #  add_node method...?

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

pprint(graph2._as_dict())
