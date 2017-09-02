# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self is None:
            return "Nil"
        else:
            return "%s -> %s" % (self.val, repr(self.next))

# 思路:通过指定两个指针,两者间距n, 这样当一个到达尾部,另一个就是指向尾部向前n的node.
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head

        first, second = dummy, dummy

        for _ in range(n):
            first = first.next

        while first.next:
            first, second = first.next, second.next

        second.next = second.next.next

        return dummy.next


# # 另一种思路: 给每个node index, 然后把移除的node前面的node的值都覆盖到下一个上.
# class Solution:
#     def removeNthFromEnd(self, head, n):
#         def remove(head):
#             if not head:
#                 return 0, head
#             i, head.next = remove(head.next)
#             return i+1, (head, head.next)[i+1 == n]
#         return remove(head)[1]


if __name__ == "__main__":
    head = ListNode(1)
    # head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    # # print head

    print Solution().removeNthFromEnd(head, 1)



