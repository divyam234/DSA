
# https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        slow = fast = node = head
        
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast: break
        else:
            return None
        
        while node is not slow:
            node, slow = node.next, slow.next
        return node