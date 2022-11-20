from tkinter.messagebox import NO
from turtle import pd


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    def reverseList(self):
        prev = self.head
        curr = self.head.next
        next = None

        while curr.next:
            next = curr.next
            curr.next = prev 
            prev = curr
            curr = next

        self.head.next=None
        next.next=prev
        self.head=next
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next
        
llist = LinkedList()
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print('Actual')
llist.display()
llist.reverseList()
print('Reverse')
llist.display()