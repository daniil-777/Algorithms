class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersect = []
        hash_1 = {}
        hash_2 = {}
        for el in nums1:
            if el not in hash_1.keys():
                hash_1[el] = 1
                
        for el in nums2:
            if el in hash_1.keys() and el not in intersect:
                intersect.append(el)
                
        return intersect