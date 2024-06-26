class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
        }
        
        value = 0
        i = 0
        while i<len(s):
            if i < len(s) - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                value +=  roman_map[s[i + 1]] - roman_map[s[i]]
                i += 2
            else:
                value += roman_map[s[i]]
                i +=1
    
        return value

