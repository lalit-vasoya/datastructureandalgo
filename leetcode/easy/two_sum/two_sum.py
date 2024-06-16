class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i, val_i in enumerate(nums):
            for j in range(i+1, length):
                if val_i + nums[j]==target:
                    print(val_i, nums[j])
                    return [i, j]

