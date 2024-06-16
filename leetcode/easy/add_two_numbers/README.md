You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example 1:**

 ![](https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg)

**Input:** l1 = \[2,4,3\], l2 = \[5,6,4\]
**Output:** \[7,0,8\]
**Explanation:** 342 + 465 = 807.

**Example 2:**

**Input:** l1 = \[0\], l2 = \[0\]
**Output:** \[0\]

**Example 3:**

**Input:** l1 = \[9,9,9,9,9,9,9\], l2 = \[9,9,9,9\]
**Output:** \[8,9,9,9,0,0,0,1\]

**Constraints:**

* The number of nodes in each linked list is in the range `[1, 100]`.
* `0 <= Node.val <= 9`
* It is guaranteed that the list represents a number that does not have leading zeros.


## [Solution](https://pythontutor.com/visualize.html#code=%23%20Definition%20for%20singly-linked%20list.%0Aclass%20ListNode%3A%0A%20%20%20%20def%20__init__%28self,%20val%3D0,%20next%3DNone%29%3A%0A%20%20%20%20%20%20%20%20self.val%20%3D%20val%0A%20%20%20%20%20%20%20%20self.next%20%3D%20next%0A%0A%20%20%20%20def%20__str__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f'val%3A%7Bself.val%7D,next%3A%7Bself.next%7D'%0A%0A%0Aclass%20Solution%3A%0A%20%20%20%20def%20addTwoNumbers%28self,%20l1,%20l2%29%3A%0A%20%20%20%20%20%20%20%20carry%20%3D%200%0A%20%20%20%20%20%20%20%20head%20%3D%20ListNode%28%29%20%23%20starting%20node%0A%20%20%20%20%20%20%20%20curr%20%3D%20head%20%23%20store%20head%20ass%20current%0A%0A%20%20%20%20%20%20%20%20while%20l1%20or%20l2%20or%20carry%3A%20%23%20while%20run%20till%20l1,%20l2%20or%20carry%20not%20have%20truth%20value%0A%20%20%20%20%20%20%20%20%20%20%20%20first%20%3D%200%0A%20%20%20%20%20%20%20%20%20%20%20%20second%20%3D%200%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20l1%3A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20first%20%3D%20l1.val%20%23%20assign%20node%20value%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20l1%20%3D%20l1.next%20%23%20move%20to%20next%20node%20after%20grabbing%20value%20%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20l2%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20second%20%3D%20l2.val%20%23%20assign%20node%20value%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20l2%20%3D%20l2.next%20%23%20move%20to%20next%20node%20after%20grabbing%20value%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20val%20%3D%20carry%20%2B%20first%20%2B%20second%20%23%20sum%20of%20carry%20and%20value%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20carry%20%3D%20val%20//%2010%20%23%20get%20carry%20%0A%20%20%20%20%20%20%20%20%20%20%20%20val%20%3D%20val%20%25%2010%20%23%20get%20left%20value%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20storing%20val%20in%20link-list%0A%20%20%20%20%20%20%20%20%20%20%20%20curr.next%20%3D%20ListNode%28val%29%0A%20%20%20%20%20%20%20%20%20%20%20%20curr%20%3D%20curr.next%20%23%0A%20%20%20%20%20%20%20%20return%20head.next%0A%0A%23%20uncomment%20following%20code%20for%20testing%0A%0Adef%20prepare_input%28l%29%3A%0A%20%20%20%20head%20%3D%20ListNode%28l%5B0%5D%29%0A%20%20%20%20first%20%3D%20head%0A%20%20%20%20for%20i%20in%20l%5B1%3A%5D%3A%0A%20%20%20%20%20%20%20%20node%20%3D%20ListNode%28i%29%0A%20%20%20%20%20%20%20%20first.next%20%3D%20node%0A%20%20%20%20%20%20%20%20first%20%3D%20node%0A%20%20%20%20return%20head%0A%20%20%20%20%0Al1%20%3D%20prepare_input%28%5B2,4,3%5D%29%0Al2%20%3D%20prepare_input%28%5B5,6,4%5D%29%0Aoutput%20%3D%20Solution%28%29.addTwoNumbers%28l1,%20l2%29%0A%0Awhile%20output%3A%0A%20%20%20%20print%28output.val,%20'-------'%29%0A%20%20%20%20output%20%3D%20output.next&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

