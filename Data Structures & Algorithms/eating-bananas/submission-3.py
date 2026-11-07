class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        answer = right

        while left <= right:
            middle = left + (right - left) // 2
            hours = 0

            for pile in piles:
                hours += (pile + middle - 1) // middle
            
            if hours > h:
                left = middle + 1
            else:
                answer = middle
                right = middle - 1

        return answer
                




        