

class ListNode:
    """Definition for singly-linked list"""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        res = [self.val]
        next_item = self.next
        while next_item is not None:
            res.append(next_item.val)
            next_item = next_item.next

        return f"{res!r}"


class NonRecursiveSolution:

    @staticmethod
    def list_node2int(list_node: ListNode) -> int:
        next_item = list_node.next
        res = [str(list_node.val)]

        while next_item is not None:
            res.append(str(next_item.val))
            next_item = next_item.next

        return int("".join(res[::-1]))

    @staticmethod
    def int2list_node(number: int) -> ListNode:
        res = None
        for item in str(number):
            res = ListNode(val=int(item), next=res)
        return res

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.int2list_node(self.list_node2int(l1) + self.list_node2int(l2))


class RecursiveSolution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> [ListNode, None]:
        # the end of recursion
        if l1 is None and l2 is None:
            return None

        if not l1:
            l1 = ListNode()

        if not l2:
            l2 = ListNode()

        new_val = l1.val + l2.val

        if new_val >= 10:
            next_node = l1.next or l2.next or ListNode()
            next_node.val += 1

            if not l1.next and not l2.next:
                l1.next = next_node

            new_val = new_val % 10

        return ListNode(val=new_val, next=self.addTwoNumbers(l1.next, l2.next))


def main():
    # Example 1:
    # Input: l1 = [2,4,3], l2 = [5,6,4]
    # Output: [7,0,8]
    # Explanation: 342 + 465 = 807.
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    print(f"Linked lists: {l1}\t{l2}, expected [7,0,8]")
    print(RecursiveSolution().addTwoNumbers(l1=l1, l2=l2))
    print('-----------------')

    # Example 2:
    # Input: l1 = [0], l2 = [0]
    # Output: [0]
    l1 = ListNode(0,)
    l2 = ListNode(0,)
    print(f"Linked lists: {l1}\t{l2}, expected [0]")
    print(RecursiveSolution().addTwoNumbers(l1=l1, l2=l2))
    print('-----------------')

    # Example 3:
    # Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    # Output: [8,9,9,9,0,0,0,1]
    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    print(f"Linked lists: {l1}\t{l2}, expected [8,9,9,9,0,0,0,1]")
    print(RecursiveSolution().addTwoNumbers(l1=l1, l2=l2))


if __name__ == '__main__':
    main()
