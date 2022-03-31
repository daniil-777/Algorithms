class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        d = [0 for i in range(target + 1)]
        d[0] = 1       
        for j in range(1, target + 1):
            d[j] = sum([d[j - i] for i in nums if j >= i])
            print("d[j]: ", d[j])
        return d[-1]