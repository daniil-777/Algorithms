class Solution:
    def numSplits(self, s: str) -> int:
        len_str = len(s)
        hash_l = {}
        hash_r = {}
        unique_l = 0
        unique_r = 0
        n_splits = 0
        
        for i in range(26):
            hash_l[i] = 0
            hash_r[i] = 0
        
        for el in s:
            if hash_r[ord(el) - ord('a')] == 0:
                unique_r += 1
                
           
            hash_r[ord(el) - ord('a')] +=1
        
        
        # for ind in range(len(s)):
        #     if hash_l[]
        
        for el in s:
            if hash_l[ord(el) - ord('a')] == 0:
                unique_l += 1
            hash_l[ord(el) - ord('a')] += 1
            hash_r[ord(el) - ord('a')] -= 1
            
            if hash_r[ord(el) - ord('a')] == 0:
                unique_r -= 1
            
            if unique_l == unique_r:
                n_splits += 1
                
        return n_splits