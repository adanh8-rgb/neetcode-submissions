class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       hashmap = {}

       for i, n in enumerate(nums):
        remain = target - n
        if remain in hashmap:
            return [hashmap[remain], i]
        
        
        hashmap[n] = i
        