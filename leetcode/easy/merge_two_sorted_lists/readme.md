You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return _the head of the merged linked list_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

**Input:** list1 = \[1,2,4\], list2 = \[1,3,4\]
**Output:** \[1,1,2,3,4,4\]

**Example 2:**

**Input:** list1 = \[\], list2 = \[\]
**Output:** \[\]

**Example 3:**

**Input:** list1 = \[\], list2 = \[0\]
**Output:** \[0\]

**Constraints:**

*   The number of nodes in both lists is in the range `[0, 50]`.
*   `-100 <= Node.val <= 100`
*   Both `list1` and `list2` are sorted in **non-decreasing** order.

## ![Solution](https://pythontutor.com/visualize.html#code=%23%20Definition%20for%20singly-linked%20list.%0Aclass%20ListNode%3A%0A%20%20%20%20def%20__init__%28self,%20val%3D0,%20next%3DNone%29%3A%0A%20%20%20%20%20%20%20%20self.val%20%3D%20val%0A%20%20%20%20%20%20%20%20self.next%20%3D%20next%0A%0A%0Aclass%20Solution%3A%0A%20%20%20%20def%20mergeTwoLists%28self,%20list1,%20list2%29%3A%0A%20%20%20%20%20%20%20%20head%20%3D%20ListNode%28%29%0A%20%20%20%20%20%20%20%20dummy%20%3D%20head%0A%20%20%20%20%20%20%20%20while%20list1%20and%20list2%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20list1.val%20%3E%3D%20list2.val%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20dummy.next%20%3D%20list2%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20list2%20%3D%20list2.next%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20dummy.next%20%3D%20list1%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20list1%20%3D%20list1.next%0A%20%20%20%20%20%20%20%20%20%20%20%20dummy%20%3D%20dummy.next%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20if%20list1%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20dummy.next%20%3D%20list1%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20dummy.next%20%3D%20list2%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20return%20head.next%0A%0A%0A%23%20uncomment%20following%20code%20for%20testing%0A%0Adef%20prepare_input%28l%29%3A%0A%20%20%20%20head%20%3D%20ListNode%28l%5B0%5D%29%0A%20%20%20%20first%20%3D%20head%0A%20%20%20%20for%20i%20in%20l%5B1%3A%5D%3A%0A%20%20%20%20%20%20%20%20node%20%3D%20ListNode%28i%29%0A%20%20%20%20%20%20%20%20first.next%20%3D%20node%0A%20%20%20%20%20%20%20%20first%20%3D%20node%0A%20%20%20%20return%20head%0A%20%20%20%20%0Al1%20%3D%20prepare_input%28%5B1,2,3%5D%29%0Al2%20%3D%20prepare_input%28%5B1,3,4%5D%29%0Aoutput%20%3D%20Solution%28%29.mergeTwoLists%28l1,%20l2%29%0A%0Awhile%20output%3A%0A%20%20%20%20print%28output.val,%20'-------'%29%0A%20%20%20%20output%20%3D%20output.next&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)