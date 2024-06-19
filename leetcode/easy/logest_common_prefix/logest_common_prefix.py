class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return strs[0][:self._get_length(strs)]

    def _get_length(self, strs: List[str]):
        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i < len(string) and strs[0][i]==string[i]:
                    continue    
                return i
