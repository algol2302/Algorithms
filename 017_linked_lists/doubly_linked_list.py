class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        """It insert item at the end. O(1)"""

        new_node = Node(data=data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def traverse_forward(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next

    def traverse_backward(self):
        actual_node = self.tail

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.previous


if __name__ == '__main__':
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.insert(1)
    doubly_linked_list.insert(2)
    doubly_linked_list.insert(3)

    doubly_linked_list.traverse_forward()
    print('---------')
    doubly_linked_list.traverse_backward()
