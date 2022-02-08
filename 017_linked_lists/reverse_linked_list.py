from main import LinkedList


class LinkedListWithReverse(LinkedList):
    def brute_force_reverse(self) -> LinkedList:
        _linked_list = LinkedList()
        actual_node = self.head

        while actual_node is not None:
            _linked_list.insert_start(actual_node.data)
            actual_node = actual_node.next_node

        return _linked_list

    def reverse(self) -> None:
        current_node = self.head
        previous_node = None

        while current_node:
            # remember next node for iterating
            next_node = current_node.next_node
            # swap nodes
            current_node.next_node, previous_node = previous_node, current_node
            # move to the next node
            current_node = next_node

        self.head = previous_node


def main():
    # naive approach
    linked_list = LinkedListWithReverse()
    linked_list.insert_start(4)
    linked_list.insert_start(3.2)
    linked_list.insert_start("Test")
    linked_list.insert_end(10)
    linked_list.insert_end(100)
    linked_list.insert_end(1000)
    linked_list.traverse()
    # naive solution
    # print('-------------------------')
    # new_linked_list = linked_list.brute_force_reverse()
    # new_linked_list.traverse()
    print("-------------------------")
    linked_list.reverse()
    linked_list.traverse()


if __name__ == "__main__":
    main()
