class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i in range(len(nums)):
            for j in range(len(nums)+1):
                if nums[i] + nums[j] == target:
                    answer = [i, j]
                    return answer

 