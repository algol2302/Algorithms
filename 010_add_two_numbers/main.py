

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


class Solution:

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
        _res = str(number)
        res = None
        for item in _res:
            res = ListNode(val=int(item), next=res)
        return res

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.int2list_node(self.list_node2int(l1) + self.list_node2int(l2))


def main():
    # Example 1:
    # Input: l1 = [2,4,3], l2 = [5,6,4]
    # Output: [7,0,8]
    # Explanation: 342 + 465 = 807.
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))

    print(f"Linked lists: {l1}\t{l2}")
    print(Solution().addTwoNumbers(l1=l1, l2=l2))

    # addTwoNumbers()

    # Example 2:
    # Input: l1 = [0], l2 = [0]
    # Output: [0]

    # Example 3:
    # Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    # Output: [8,9,9,9,0,0,0,1]


if __name__ == '__main__':
    main()
