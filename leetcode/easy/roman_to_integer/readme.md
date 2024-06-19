Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

| **Symbol** | **Value** |
|-------|---------|
| I     | 1       |
| V     | 5       |
| X     | 10      |
| L     | 50      |
| C     | 100     |
| D     | 500     |
| M     | 1000    |

For example, `2` is written as `II` in Roman numeral, just two ones added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

*   `I` can be placed before `V` (5) and `X` (10) to make 4 and 9. 
*   `X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 
*   `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

**Example 1:**

**Input:** s = "III"
**Output:** 3
**Explanation:** III = 3.

**Example 2:**

**Input:** s = "LVIII"
**Output:** 58
**Explanation:** L = 50, V= 5, III = 3.

**Example 3:**

**Input:** s = "MCMXCIV"
**Output:** 1994
**Explanation:** M = 1000, CM = 900, XC = 90 and IV = 4.

**Constraints:**

*   `1 <= s.length <= 15`
*   `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.
*   It is **guaranteed** that `s` is a valid roman numeral in the range `[1, 3999]`.

---
## [Solution](https://pythontutor.com/visualize.html#code=class%20Solution%3A%0A%20%20%20%20def%20romanToInt%28self,%20s%3A%20str%29%20-%3E%20int%3A%0A%20%20%20%20%20%20%20%20roman_map%20%3D%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22I%22%3A%201,%20%22V%22%3A%205,%20%22X%22%3A%2010,%20%22L%22%3A%2050,%20%22C%22%3A%20100,%20%22D%22%3A%20500,%20%22M%22%3A%201000%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20value%20%3D%200%0A%20%20%20%20%20%20%20%20i%20%3D%200%0A%20%20%20%20%20%20%20%20while%20i%3Clen%28s%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20i%20%3C%20len%28s%29%20-%201%20and%20roman_map%5Bs%5Bi%5D%5D%20%3C%20roman_map%5Bs%5Bi%20%2B%201%5D%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20value%20%2B%3D%20%20roman_map%5Bs%5Bi%20%2B%201%5D%5D%20-%20roman_map%5Bs%5Bi%5D%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20i%20%2B%3D%202%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20value%20%2B%3D%20roman_map%5Bs%5Bi%5D%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20i%20%2B%3D1%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20return%20value&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
