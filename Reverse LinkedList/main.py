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