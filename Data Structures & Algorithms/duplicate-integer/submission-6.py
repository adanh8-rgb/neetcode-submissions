class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
     dictt = {}

     for num in nums:
         if num in dictt:
             return True
         dictt[num] = 0
     return False

     
     



        