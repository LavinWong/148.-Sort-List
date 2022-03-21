# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        # if list if empty or catains just one element
        if not head or not head.next:
            return head
        
        #Split the list to two list, the one is head to the mid and other is mid+1 to the rest.
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp
        
        #Split the list again, until the list just have one element./
        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left,right)


    def getMid(self,head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


    def merge(self, left, right):
        tail = dummy = ListNode()
        #We add the element one by one, so when it finshed it will be sorted.
        while left and right:
            if left.val<right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next

            tail = tail.next
        
        if left:
            tail.next = left
        
        if right:
            tail.next = right
        
        return dummy.next
