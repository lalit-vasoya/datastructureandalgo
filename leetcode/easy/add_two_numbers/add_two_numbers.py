# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#     def __str__(self):
#         return f'val:{self.val},next:{self.next}'


class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        head = ListNode() # starting node
        curr = head # store head ass current

        while l1 or l2 or carry: # while run till l1, l2 or carry not have truth value
            first = 0
            second = 0
            if l1:    
                first = l1.val # assign node value
                l1 = l1.next # move to next node after grabbing value 
            if l2:
                second = l2.val # assign node value
                l2 = l2.next # move to next node after grabbing value

            val = carry + first + second # sum of carry and value
            
            carry = val // 10 # get carry 
            val = val % 10 # get left value 
            
            # storing val in link-list
            curr.next = ListNode(val)
            curr = curr.next #
        return head.next

# uncomment following code for testing

# def prepare_input(l):
#     head = ListNode(l[0])
#     first = head
#     for i in l[1:]:
#         node = ListNode(i)
#         first.next = node
#         first = node
#     return head
    
# l1 = prepare_input([2,4,3])
# l2 = prepare_input([5,6,4])
# output = Solution().addTwoNumbers(l1, l2)

# while output:
#     print(output.val, '-------')
#     output = output.next

