class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        already = set();
        for i in nums:
            if i in already:
                return True
            already.add(i)
        return False
        