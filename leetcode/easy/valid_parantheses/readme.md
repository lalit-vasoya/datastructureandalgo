Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1.  Open brackets must be closed by the same type of brackets.
2.  Open brackets must be closed in the correct order.
3.  Every close bracket has a corresponding open bracket of the same type.

**Example 1:**

**Input:** s = "()"
**Output:** true

**Example 2:**

**Input:** s = "()\[\]{}"
**Output:** true

**Example 3:**

**Input:** s = "(\]"
**Output:** false

**Constraints:**

*   `1 <= s.length <= 104`
*   `s` consists of parentheses only `'()[]{}'`.

## [Solution](https://pythontutor.com/visualize.html#code=class%20Solution%3A%0A%20%20%20%20def%20isValid%28self,%20s%3A%20str%29%20-%3E%20bool%3A%0A%20%20%20%20%20%20%20%20mapped%20%3D%20%7B%22%28%22%3A%20%22%29%22,%20%22%7B%22%3A%22%7D%22,%20%22%5B%22%3A%22%5D%22%7D%0A%20%20%20%20%20%20%20%20arr%20%3D%20%5B%5D%0A%20%20%20%20%20%20%20%20flag%20%3D%20True%0A%20%20%20%20%20%20%20%20for%20char%20in%20s%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20val%20%3D%20mapped.get%28char%29%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20val%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20arr.append%28val%29%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20len%28arr%29%3D%3D0%20or%20arr.pop%28%29%20!%3D%20char%3A%20%20%23%20correct%20order%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20False%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20return%20len%28arr%29%3D%3D0%0A%0Aprint%28Solution%28%29.isValid%28%22%5D%22%29%29%0Aprint%28Solution%28%29.isValid%28%22%28%29%22%29%29%0Aprint%28Solution%28%29.isValid%28%22%28%28%28%28%22%29%29%0Aprint%28Solution%28%29.isValid%28%22%28%29%7B%7D%22%29%29%0Aprint%28Solution%28%29.isValid%28%22%5D%5D%5D%5D%22%29%29%0Aprint%28Solution%28%29.isValid%28%22%7B%5B%5D%7D%22%29%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

