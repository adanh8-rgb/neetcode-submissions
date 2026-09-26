#I need to be able to loop through the list one time and see if the
#list has duplicates 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
     return len(set(nums)) != len(nums)

     



     
     



        