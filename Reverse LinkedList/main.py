# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev=None
        if head != None:
            current=head
        else:
            return None
        while True:
            next1,current.next=current.next,prev
            prev = current
            if next1 != None:
                current=next1
            else:
                return current
            
class Solution2(object):
    def reverseList(self, head):
        prev_node = None
        current_node = head

        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        return prev_node