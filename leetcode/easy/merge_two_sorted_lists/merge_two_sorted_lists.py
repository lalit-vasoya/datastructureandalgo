# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        dummy = head
        while list1 and list2:
            if list1.val >= list2.val:
                dummy.next = list2
                list2 = list2.next
            else:
                dummy.next = list1
                list1 = list1.next
            dummy = dummy.next
        
        if list1:
            dummy.next = list1
        else:
            dummy.next = list2
               
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
    
# l1 = prepare_input([1,2,3])
# l2 = prepare_input([1,3,4])
# output = Solution().mergeTwoLists(l1, l2)

# while output:
#     print(output.val, '-------')
#     output = output.next