Given an array of integers `nums` and an integer `target`, return _indices of the two numbers such that they add up to `target`_.

You may assume that each input would have **_exactly_ one solution**, and you may not use the _same_ element twice.

You can return the answer in any order.

**Example 1:**

**Input:** nums = \[2,7,11,15\], target = 9
**Output:** \[0,1\]
**Explanation:** Because nums\[0\] + nums\[1\] == 9, we return \[0, 1\].

**Example 2:**

**Input:** nums = \[3,2,4\], target = 6
**Output:** \[1,2\]

**Example 3:**

**Input:** nums = \[3,3\], target = 6
**Output:** \[0,1\]

**Constraints:**

*   `2 <= nums.length <= 104`
*   `-109 <= nums[i] <= 109`
*   `-109 <= target <= 109`
*   **Only one valid answer exists.**

**Follow-up:** Can you come up with an algorithm that is less than `O(n2)` time complexity?

![](https://pythontutor.com/visualize.html#code=class%20Solution%3A%0A%20%20%20%20def%20twoSum%28self,%20nums%3A%20List%5Bint%5D,%20target%3A%20int%29%20-%3E%20List%5Bint%5D%3A%0A%20%20%20%20%20%20%20%20length%20%3D%20len%28nums%29%0A%20%20%20%20%20%20%20%20for%20i,%20val_i%20in%20enumerate%28nums%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20for%20j%20in%20range%28i%2B1,%20length%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20val_i%20%2B%20nums%5Bj%5D%3D%3Dtarget%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28val_i,%20nums%5Bj%5D%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20%5Bi,%20j%5D&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
