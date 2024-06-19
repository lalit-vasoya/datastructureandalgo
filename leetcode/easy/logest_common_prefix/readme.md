Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

**Example 1:**

**Input:** strs = \["flower","flow","flight"\]
**Output:** "fl"

**Example 2:**

**Input:** strs = \["dog","racecar","car"\]
**Output:** ""
**Explanation:** There is no common prefix among the input strings.

**Constraints:**

*   `1 <= strs.length <= 200`
*   `0 <= strs[i].length <= 200`
*   `strs[i]` consists of only lowercase English letters.

---
## [Solution](https://pythontutor.com/visualize.html#code=class%20Solution%3A%0A%20%20%20%20def%20longestCommonPrefix%28self,%20strs%29%20-%3E%20str%3A%0A%20%20%20%20%20%20%20%20return%20strs%5B0%5D%5B%3Aself._get_length%28strs%29%5D%0A%0A%20%20%20%20def%20_get_length%28self,%20strs%29%3A%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%28len%28strs%5B0%5D%29%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20for%20string%20in%20strs%5B1%3A%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20i%20%3C%20len%28string%29%20and%20strs%5B0%5D%5Bi%5D%3D%3Dstring%5Bi%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20continue%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20i&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)