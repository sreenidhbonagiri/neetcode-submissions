class Solution:
    # Here you can go through the list, then once you find the value, you can append it immediately into a result list. Then you can go back to the list and append the rest of the values so that the value would be at the end. Then you can search through the new list and just return the index of where the first occurence of the value is
    def removeElement(self, nums: List[int], val: int) -> int:
        result = []

        for num in nums:
            if num != val:
                result.append(num)

        for i in range(len(result)):
            nums[i] = result[i]
        return len(result)
            