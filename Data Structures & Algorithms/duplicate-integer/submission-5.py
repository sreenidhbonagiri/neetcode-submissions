class Solution:
    # Plan:
    # We could go through the list, and put each element into another list.
    # Now while we are inputting the elements into the list we can check if that element is already in the list or not.
    # So if it is already in the list, then we can return false, otherwise return true
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for element in nums:
            if element in seen:
                return True
            seen.add(element)
    

        return False
      