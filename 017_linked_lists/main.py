class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.number_of_nodes = 0

    def insert_start(self, data):
        self.number_of_nodes += 1

        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_end(self, data):
        self.number_of_nodes += 1

        new_node = Node(data)

        actual_node = self.head

        while actual_node.next_node is not None:
            actual_node = actual_node.next_node

        actual_node.next_node = new_node

    def size_of(self):
        return self.number_of_nodes

    def traverse(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next_node


def main():
    linked_list = LinkedList()
    linked_list.insert_start(4)
    linked_list.insert_start(3.2)
    linked_list.insert_start('Test')
    linked_list.insert_end(10)
    linked_list.insert_end(100)
    linked_list.insert_end(1000)

    linked_list.traverse()

if __name__ == '__main__':
    main()
