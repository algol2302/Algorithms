from main import Node, LinkedList


class OverridenLinkedList(LinkedList):
    def get_middle_node(self):

        fast_pointer = self.head
        slow_pointer = self.head

        while fast_pointer.next_node and fast_pointer.next_node.next_node:
            fast_pointer = fast_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node

        return slow_pointer


def search_middle_node_0(linked_list: LinkedList) -> Node:
    """Brute-force solution"""

    middle = linked_list.number_of_nodes // 2 - 1
    actual_node = linked_list.head
    for _ in range(middle):
        actual_node = actual_node.next_node

    return actual_node


def main():
    # naive approach
    linked_list = LinkedList()
    linked_list.insert_start(4)
    linked_list.insert_start(3.2)
    linked_list.insert_start("Test")
    linked_list.insert_end(10)
    linked_list.insert_end(100)
    linked_list.insert_end(1000)
    linked_list.traverse()
    print(f"Size: {linked_list.number_of_nodes}")
    print(f"Middle node: {search_middle_node_0(linked_list)}")
    print("-------------------------")
    # faster approach
    linked_list = OverridenLinkedList()
    linked_list.insert_start(4)
    linked_list.insert_start(3.2)
    linked_list.insert_start("Test")
    linked_list.insert_end(10)
    linked_list.insert_end(100)
    linked_list.insert_end(1000)
    linked_list.traverse()
    print(f"Size: {linked_list.number_of_nodes}")
    print(f"Middle node: {linked_list.get_middle_node()}")


if __name__ == "__main__":
    main()
