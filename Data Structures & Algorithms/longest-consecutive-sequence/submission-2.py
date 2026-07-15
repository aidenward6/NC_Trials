class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        counter=1
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i+1]:
                counter = counter + 1
                
            else:
                counter = counter
        return counter