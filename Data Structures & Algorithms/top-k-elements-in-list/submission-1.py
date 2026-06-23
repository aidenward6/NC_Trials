class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # 1. Build the frequency dictionary
        count_dict = {}
        for n in nums:
            count_dict[n] = count_dict.get(n, 0) + 1
        
        # 2. Sort the dictionary items by their values (counts) in descending order
        # x[1] refers to the value in the (key, value) tuple
        sorted_items = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
        
        # 3. Extract the first k keys
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])
            
        return result