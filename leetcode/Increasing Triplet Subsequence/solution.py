class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # print("nums: ", nums)
        if len(nums) < 3:
            return False
        minOne = 100000000000000
        maxOne = 100000000000000
        for el in nums:
            if el < minOne:
                minOne = el
            if el > minOne:
                maxOne = min(el, maxOne)
            if el > maxOne:
                # print("happened!")
                return True
        return False