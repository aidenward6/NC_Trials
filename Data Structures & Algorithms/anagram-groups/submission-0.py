class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
    
        for word in strs:
            found_group = False
            for group in result:
                # Compare current word with a representative of the group
                if sorted(word) == sorted(group[0]):
                    group.append(word)
                    found_group = True
                    break
            
            # If no group was found, start a new one
            if not found_group:
                result.append([word])
                
        return result