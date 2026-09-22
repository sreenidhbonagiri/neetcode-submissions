class Solution:
   
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = set()
        for num in nums:
            if num not in dupes:
                dupes.add(num)
            else:
                return True

        return False
      