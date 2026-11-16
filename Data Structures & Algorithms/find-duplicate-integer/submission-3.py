class Solution:
    # So we need to use slow and fast where slow moves at one number at a time where as fast moves double that pace, and each iteration we need to check if they are ever equal which shows that we have a cycle? And then we keep fast the same, but we move slow to 0, and restart this time we move both pointers at the same time. And once they meet that would be the entrance to the cycle.
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


        
        
        