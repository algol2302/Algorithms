from main import LinkedList, Node


def search_middle_node_0(linked_list: LinkedList) -> Node:
    """Brute-force solution"""

    middle = linked_list.number_of_nodes // 2 - 1
    actual_node = linked_list.head
    for _ in range(middle):
        actual_node = actual_node.next_node

    return actual_node


def main():
    linked_list = LinkedList()
    linked_list.insert_start(4)
    linked_list.insert_start(3.2)
    linked_list.insert_start('Test')
    linked_list.insert_end(10)
    linked_list.insert_end(100)
    linked_list.insert_end(1000)
    linked_list.traverse()
    print(f"Size: {linked_list.number_of_nodes}")
    print(f"Middle node: {search_middle_node_0(linked_list)}")


if __name__ == '__main__':
    main()
