class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        true = True
        false = False
        nums.sort()
        
        for i in range(len(nums) - 1):
            temp = nums[i]
            if nums[i+1] == temp:
                return true
        return false