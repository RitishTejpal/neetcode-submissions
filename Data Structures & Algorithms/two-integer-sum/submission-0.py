class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = defaultdict(int)
        for i in range(len(nums)):
            num = nums[i]
            if target - num in mp:
                return [mp[target - num], i]
            mp[num] = i
        
        return []