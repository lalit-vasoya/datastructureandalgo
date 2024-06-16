Given an integer `x`, return `true` _if_ `x` _is a_

_**palindrome**_

_, and_ `false` _otherwise_.

**Example 1:**

**Input:** x = 121
**Output:** true
**Explanation:** 121 reads as 121 from left to right and from right to left.

**Example 2:**

**Input:** x = -121
**Output:** false
**Explanation:** From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

**Example 3:**

**Input:** x = 10
**Output:** false
**Explanation:** Reads 01 from right to left. Therefore it is not a palindrome.

**Constraints:**

*   `-231 <= x <= 231 - 1`

**Follow up:** Could you solve it without converting the integer to a string?

## [Solution](https://pythontutor.com/visualize.html#code=class%20Solution%3A%0A%20%20%20%20def%20isPalindrome%28self,%20x%3A%20int%29%20-%3E%20bool%3A%0A%20%20%20%20%20%20%20%20%23%20return%200%20if%20x%20is%20negative%0A%20%20%20%20%20%20%20%20if%20x%3C0%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20False%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%23%20reverse%20the%20number%20base%0A%20%20%20%20%20%20%20%20rev%20%3D%200%0A%20%20%20%20%20%20%20%20y%3Dx%0A%20%20%20%20%20%20%20%20while%20x!%3D0%3A%20%23%20run%20till%20x%20get%20zero%0A%20%20%20%20%20%20%20%20%20%20%20%20rev%20%3D%20%28rev%20*%2010%29%20%2B%20x%2510%0A%20%20%20%20%20%20%20%20%20%20%20%20x%20//%3D%2010%0A%20%20%20%20%20%20%20%20return%20rev%3D%3Dy&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)