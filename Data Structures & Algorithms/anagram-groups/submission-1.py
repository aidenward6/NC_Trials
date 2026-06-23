class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
    
        for word in strs:
            # Create the signature (label) by sorting
            label = "".join(sorted(word))
            
            # If label is NOT in dictionary, create an empty list for it
            if label not in anagrams:
                anagrams[label] = []
            
            # Now it is safe to append the word to the list
            anagrams[label].append(word)
            
        # Return all the lists stored in the dictionary
        return list(anagrams.values())