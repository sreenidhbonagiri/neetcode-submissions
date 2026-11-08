class Solution:
    # so for 
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        answer = right
        

        while left <= right:
            hours = 0
            middle = left + (right - left) // 2

            for pile in piles:
                hours += (pile + middle - 1) // middle

            if hours > h:
                left = middle + 1
            else:
                answer = middle
                right = middle - 1

        return answer

                
                



        
        